-- CreateTable
CREATE TABLE "employee" (
    "id" TEXT NOT NULL,
    "firstname" TEXT NOT NULL,
    "lastname" TEXT NOT NULL,
    "published" BOOLEAN NOT NULL,
    "desc" TEXT,

    CONSTRAINT "employee_pkey" PRIMARY KEY ("id")
);
