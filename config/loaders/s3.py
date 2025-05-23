# Código de ejemplo comentado:
# s3 = boto3.client('s3')
# obj = s3.get_object(Bucket="tu-bucket", Key=f"{env}/app.yml")
# data = yaml.safe_load(obj['Body'])
# return AppConfig(**data["app"])