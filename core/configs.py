import dotenv

env_vars = dotenv.Dotenv(".env")


class Settings:
    DB_NAME: str = env_vars.get("DB_NAME")
    DB_SERVER: str = env_vars.get("DB_SERVER")
    DB_DRIVER: str = "ODBC Driver 17 for SQL Server"
