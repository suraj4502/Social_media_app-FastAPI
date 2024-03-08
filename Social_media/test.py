from urllib.parse import quote_plus

password = "Suraj@425@4502"
encoded_password = quote_plus(password)
print(encoded_password)
# Use encoded_password in your database URL

# user=postgres.vkzmrbgiibbyjjzwtcgh password=[YOUR-PASSWORD] host=aws-0-ap-south-1.pooler.supabase.com port=5432 dbname=postgres

# Connect to Supabase via connection pooling with Supavisor.
DATABASE_URL="postgres://postgres.vkzmrbgiibbyjjzwtcgh:[YOUR-PASSWORD]@aws-0-ap-south-1.pooler.supabase.com:5432/postgres"

# Direct connection to the database. Used for migrations.
DIRECT_URL="postgresql://postgres:[YOUR-PASSWORD]@db.vkzmrbgiibbyjjzwtcgh.supabase.co:5432/postgres"
        