-- CreateTable
CREATE TABLE "User" (
    "id" TEXT NOT NULL,
    "firstname" TEXT NOT NULL,
    "lastname" TEXT NOT NULL,
    "published" BOOLEAN NOT NULL,
    "desc" TEXT,

    CONSTRAINT "User_pkey" PRIMARY KEY ("id")
);
