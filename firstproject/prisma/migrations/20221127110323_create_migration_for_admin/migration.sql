-- CreateTable
CREATE TABLE "admin" (
    "id" TEXT NOT NULL,
    "username" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    "desc" TEXT,

    CONSTRAINT "admin_pkey" PRIMARY KEY ("id")
);
