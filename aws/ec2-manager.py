import boto3
import click

session = boto3.Session(profile_name='dheeraj-sa-aws')
ec2 = session.resource('ec2')

def filter_instances(project):
    instances = []

    if project:
        filters = [{'Name':'tag:Project', 'Values':[project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()

    return instances

@click.group()
def cli():
    """Manage snapshots"""

@cli.group('volumes')
def volumes():
    """Commands for volumes"""

@cli.group('snapshots')
def snapshots():
    """Commands for snapshots"""

@cli.group('instances')
def instances():
    """Commands for instances"""


@snapshots.command('list')
@click.option('--project', default=None, help="Only instance for project (tag Project:<name>)")
def list_snapshots(project):
    "List EC2 Volumes Snapshots"
    instances = filter_instances(project)

    for i in instances:
        for v in i.volumes.all():
            for s in v.snapshots.all():
                print(", ".join((s.id,
                    v.id,
                    i.id,
                    s.state,
                    s.progress,
                    s.start_time.strftime("%c")
                )))
    return

@instances.command('snapshot')
@click.option('--project', default=None, help="Only instance for project (tag Project:<name>)")
def create_snapshot(project):
    "Create snapshot for EC2 Instances"
    instances = filter_instances(project)

    for i in instances:
        for v in i.volumes.all():
            v.create_snapshot(Description="Created by EC2 Manager")
    return

@volumes.command('list')
@click.option('--project', default=None, help="Only instance for project (tag Project:<name>)")
def list_volumes(project):
    "List EC2 Volumes"
    instances = filter_instances(project)

    for i in instances:
        for v in i.volumes.all():
            print(", ".join((v.id,
            i.id,
            v.state,
            str(v.size) + 'GiB',
            v.encrypted and 'Encrypted' or 'Not Encrypted'
        )))
    return

@instances.command('start')
@click.option('--project', default=None, help="Only instance for project")
def start_instances(project):
    "Start EC2 Instances"
    instances = filter_instances(project)

    for i in instances:
        print("Starting {0}...".format(i.id))
        i.start()
    return

@instances.command('stop')
@click.option('--project', default=None, help="Only instance for project")
def stop_instances(project):
    "Stop EC2 Instances"
    instances = filter_instances(project)

    for i in instances:
        print("Stopping {0}...".format(i.id))
        i.stop()
    return

@instances.command('list')
@click.option('--project', default=None, help="Only instance for project (tag Project:<name>)")
def list_instances(project):
    "List EC2 Instances"
    instances = filter_instances(project)

    for i in instances:
        print(", ".join((i.id,
        i.instance_type,
        i.placement['AvailabilityZone'],
        i.state['Name'],
        i.public_dns_name)))

    return

if __name__ == '__main__':
    cli()
