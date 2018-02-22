#!/usr/bin/env python

import yaml
import os
import distutils.util

db_type = os.getenv('DATABASE', 'sqlite')
postgres_host = os.getenv('POSTGRES_HOST', 'db')
postgres_port = os.getenv('POSTGRES_PORT', 5432)
db_name = os.getenv('DB_NAME', 'synapse')
db_user = os.getenv('DB_USER', 'postgres')
db_pasword = os.getenv('DB_PASSWORD', '')
email_from = os.getenv('EMAIL_FROM', 'Riot EEA <eea@eea.com>')
riot_base_url =  os.getenv('RIOT_BASE_URL', '')
public_base_url =  os.getenv('PUBLIC_BASE_URL', '')
identity_url = os.getenv('IDENTITY_URL', 'http://identity:8090')
smtp_host = os.getenv('SMTP_HOST', 'postfix')
smtp_port = os.getenv('SMTP_PORT', '25')
turn_allow_guests =  os.getenv('TURN_GUESTS', False)




enable_registration = bool(distutils.util.strtobool(os.getenv('REGISTRATION_ENABLED', 'no')))

print 'DATABASE:', db_type
print 'POSTGRES_HOST:', postgres_host
print 'POSTGRES_PORT:', postgres_port
print 'DB_NAME:', db_name
print 'DB_USER:', db_user
print 'DB_PASSWORD:', db_pasword
print 'REGISTRATION_ENABLED:', enable_registration

if db_type not in ('sqlite', 'postgresql'):
    print "DATABASE env is wrong: %s" % (db_type)
    sys.exit(1)


filename = "/data/homeserver.yaml"

file = open(filename)
yaml_doc = yaml.load(file)

# default values
yaml_doc['pid_file'] = '/data/homeserver.pid'
yaml_doc['log_file'] = '/data/homeserver.log'
yaml_doc['web_client'] = False
yaml_doc['web_client_location'] = '/webclient'
yaml_doc['uploads_path'] = '/uploads'
yaml_doc['media_store_path'] = '/data/media_store'
yaml_doc['enable_registration'] = enable_registration
yaml_doc['turn_allow_guests'] = turn_allow_guests


if db_type == 'sqlite':
    yaml_doc['database'] = {'name': 'sqlite3', 'args': {'database': '/data/homeserver.db'}}
elif db_type == 'postgresql':
    yaml_doc['database'] = {'name': 'psycopg2', 'args': {'user': db_user, 'password': db_pasword, 'database': db_name, 'host': postgres_host, 'cp_min': 5, 'cp_max': 10}}

yaml_doc['email'] = {'enable_notifs': 'True', 'smtp_host': smtp_host, 'smtp_port': smtp_port, 'notif_from': email_from, 'app_name': 'Matrix', 'template_dir': '/synapse_templates', 'notif_template_html': 'notif_mail.html', 'notif_template_text': 'notif_mail.txt', 'notif_for_new_users': 'True', 'riot_base_url': riot_base_url}

yaml_doc['password_providers'] = [{ 'module': 'rest_auth_provider.RestAuthProvider', 'config': { 'endpoint': identity_url} } ]
yaml_doc['public_baseurl'] = public_base_url


with open("/data/homeserver.yaml", "w") as f:
    yaml.dump(yaml_doc, f, default_flow_style = False)
