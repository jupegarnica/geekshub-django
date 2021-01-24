ALTER DATABASE kubernetes_django OWNER TO db_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA PUBLIC TO db_user;
/* TODO
there is no clear way to make gnw_user a superuser, then migrate and then remove the superuser again, other
than from the outside. So I guess the only way to grant that it will always work is making gnw_user super user from the
start. This also only affects dev and staging since production is on its own RDS database and there user handled
separately
 */
ALTER USER db_user with SUPERUSER;