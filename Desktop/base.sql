 create Table "doctors" (
"id" serial primary key,
"lastname" varchar,
"firstname" varchar,
"middlename" varchar,
"specializations" varchar,
"phone" varchar,
"number_of_cabinet" integer,
"password" varchar
)

create Table "diagnosis" (
"id" serial primary key,
"name" varchar,
"discription" text
)

create Table "patients" (
"id" serial primary key,
"lastname" varchar,
"firstname" varchar,
"middlename" varchar,
"birthdate" date,
"passport" varchar,
"phone" varchar,
"email" varchar,
"password" varchar
)

create Table appointment(
"id" serial primary key,
"id_patients" integer,
"id_doctors" integer,
"date" date,
"time" time,
"id_diagnos" integer
)

alter table "appointment" add constraint "app_doc_id_fkey" foreign key ("id_doctors") references "doctors" ("id")
alter table "appointment" add constraint "app_pats_id_fkey" foreign key ("id_patients") references "patients" ("id")
alter table "appointment" add constraint "app_diagn_id_fkey" foreign key ("id_diagnos") references "diagnosis" ("id")
