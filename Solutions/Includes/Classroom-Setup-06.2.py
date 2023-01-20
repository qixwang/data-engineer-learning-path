# Databricks notebook source
# MAGIC %run ./_common

# COMMAND ----------

lesson_config = LessonConfig(name = None,
                             create_schema = False,
                             create_catalog = True,
                             requires_uc = True,
                             installing_datasets = True,
                             enable_streaming_support = False,
                             enable_ml_support = False)

DA = DBAcademyHelper(course_config=course_config,
                     lesson_config=lesson_config)
DA.reset_lesson()
DA.init()
DA.conclude_setup()

# COMMAND ----------

# ANSWER
try: DA.client.scim.groups.create(ANALYSTS_ROLE_NAME)
except: pass # Ignoring if it already exists

# COMMAND ----------

current_catalog = spark.sql("SELECT current_catalog() as catalog").first()[0]

DA.my_new_catalog = DA.to_catalog_name(username=DA.username, lesson_name=None)
spark.conf.set("DA.my_new_catalog", DA.my_new_catalog)
spark.conf.set("da.my_new_catalog", DA.my_new_catalog)

print(f"Current Catalog: {current_catalog}")
print(f"Your Catalog:    {DA.my_new_catalog}")


