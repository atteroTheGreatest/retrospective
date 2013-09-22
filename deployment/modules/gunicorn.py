from fabric.colors import yellow
from utils import pjoin, config, cget
from fabric.operations import run
from fabric.api import cd
from fabric.contrib.files import upload_template


COMPONENT_NAME = 'Gunicorn configuration and starting'

def started():
    upload_project_configuration()


def upload_project_configuration():
    source_file = pjoin(cget('deploy_files'), 'gunicorn',
                        'gunicorn_start')
    target_file = pjoin(cget('project_dir'), 'bin',
                        'gunicorn_start')

    print yellow('Uploading gunicorn starting script')
    upload_template(source_file, target_file, config)

    with cd(cget('project_dir')):
        run('mkdir -p run')
        run('chmod u+x bin/gunicorn_start')
        print yellow('Starting gunicorn!')
        run('./bin/gunicorn_start')

def finished():
    pass