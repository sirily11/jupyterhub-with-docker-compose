# Configuration file for jupyterhub.

# The public facing port of the proxy
c.JupyterHub.port = 8000

# Create system users that don't exist yet
c.LocalAuthenticator.create_system_users = True
c.Authenticator.add_user_cmd = [
    'adduser', '--force-badname', '-q', '--gecos', '""', '--disabled-password']
c.NotebookApp.notebook_dir = u'/home/jovyan/work'
# Set of users who can administer the Hub itself
c.Authenticator.admin_users = {'sirily11'}
