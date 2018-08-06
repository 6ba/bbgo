try:
    with open(os.path.join(BASE_DIR, "secrets.json")) as f:
        data = json.loads(f.read())
    SecretsNamedTuple = \
        namedtuple('SecretsNamedTuple', data.keys(), verbose=False)
    secrets = SecretsNamedTuple(*[data[x] for x in data.keys()])
    SECRET_KEY = getattr(secrets, "SECRET_KEY")
    DB_NAME = getattr(secrets, "DB_NAME")
    DB_USER = getattr(secrets, "DB_USER")
    DB_PASSWORD = getattr(secrets, "DB_PASSWORD")
    EMAIL_HOST = getattr(secrets, "EMAIL_HOST")
    EMAIL_HOST_USER = getattr(secrets, "EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = getattr(secrets, "EMAIL_HOST_PASSWORD")
    DEFAUL_FROM_EMAIL = getattr(secrets, "DEFAUL_FROM_EMAIL")
    SERVER_EMAIL = getattr(secrets, "SERVER_EMAIL")
    SITE_NAME = getattr(secrets, "SITE_NAME")
    SITE_LOGO = getattr(secrets, "SITE_LOGO")
    SITE_INFO = getattr(secrets, "SITE_INFO")
    ADMIN_EMAIL = getattr(secrets, "ADMIN_EMAIL")
    BLOG_CATEGORY = getattr(secrets, "BLOG_CATEGORY")
    AKISMET_API_KEY = getattr(secrets, "AKISMET_API_KEY")
    BLOG_URL = getattr(secrets, "BLOG_URL")
    SENSE_UP_CLIENT = getattr(secrets, "SENSE_UP_CLIENT")
    SENSE_UP_SLOT = getattr(secrets, "SENSE_UP_SLOT")
    SENSE_DOWN_CLIENT = getattr(secrets, "SENSE_DOWN_CLIENT")
    SENSE_DOWN_SLOT = getattr(secrets, "SENSE_DOWN_SLOT")
    SENSE_SIDE_CLIENT = getattr(secrets, "SENSE_SIDE_CLIENT")
    SENSE_SIDE_SLOT = getattr(secrets, "SENSE_SIDE_SLOT")
    FB_APP_ID = getattr(secrets, "FB_APP_ID")
except IOError:
    SECRET_KEY = 'k8n13h0y@$=v$uxg*^brlv9$#hm8w7nye6km!shc*&bkgkcd*p'
    DB_NAME = ''
    DB_USER = ''
    DB_PASSWORD = ''
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    DEFAUL_FROM_EMAIL = ''
    SERVER_EMAIL = ''
    SITE_NAME = ''
    SITE_LOGO = ''
    SITE_INFO = ''
    ADMIN_EMAIL = ''
    BLOG_CATEGORY = ''
    AKISMET_API_KEY = ''
    BLOG_URL = ''
    SENSE_UP_CLIENT = ''
    SENSE_UP_SLOT = ''
    SENSE_DOWN_CLIENT = ''
    SENSE_DOWN_SLOT = ''
    SENSE_SIDE_CLIENT = ''
    SENSE_SIDE_SLOT = ''
    FB_APP_ID = ''
finally:
    f.close()