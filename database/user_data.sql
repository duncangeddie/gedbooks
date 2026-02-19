-- MySQL dump 10.13  Distrib 8.0.45, for Linux (x86_64)
--
-- Host: localhost    Database: user_data
-- ------------------------------------------------------
-- Server version   8.0.45-0ubuntu0.24.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `chart_of_accounts`
--

DROP TABLE IF EXISTS `chart_of_accounts`;
CREATE TABLE `chart_of_accounts` (
  `user_id` int NOT NULL,
  `ref` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `created` date DEFAULT NULL,
  PRIMARY KEY (`ref`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `chart_of_accounts`
--

LOCK TABLES `chart_of_accounts` WRITE;
/*!40000 ALTER TABLE `chart_of_accounts` DISABLE KEYS */;
/*!40000 ALTER TABLE `chart_of_accounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
CREATE TABLE `customers` (
  `id` int AUTO_INCREMENT PRIMARY KEY,
  `user_id` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email_address` varchar(255) DEFAULT NULL,
  `tax_number` bigint DEFAULT NULL,
  `phone_number` bigint DEFAULT NULL,
  `address` text,
  `status` tinyint(1) DEFAULT NULL,
  `created` date DEFAULT (curdate())
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
INSERT INTO `customers` (user_id, name, email_address, tax_number, phone_number, address, status, created)
VALUES (2,'GedCom','duncan@websprout.co.za',4550123456,774992008,'Villiers Road\r\nWalmer\r\nPort Elizabeth',1,'2026-02-19');
UNLOCK TABLES;

--
-- Table structure for table `general_ledger`
--

DROP TABLE IF EXISTS `general_ledger`;
CREATE TABLE `general_ledger` (
  `user_id` int NOT NULL,
  `transaction_date` date DEFAULT NULL,
  `post_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `ref` varchar(255) DEFAULT NULL,
  `account_number` varchar(255) DEFAULT NULL,
  `account_name` varchar(255) DEFAULT NULL,
  `debit_amount` decimal(15,2) DEFAULT NULL,
  `credit_amount` decimal(15,2) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `created` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `general_ledger`
--

LOCK TABLES `general_ledger` WRITE;
/*!40000 ALTER TABLE `general_ledger` DISABLE KEYS */;
/*!40000 ALTER TABLE `general_ledger` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suppliers`
--

DROP TABLE IF EXISTS `suppliers`;
CREATE TABLE `suppliers` (
  `id` int AUTO_INCREMENT PRIMARY KEY,
  `user_id` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email_address` varchar(255) DEFAULT NULL,
  `tax_number` bigint DEFAULT NULL,
  `phone_number` bigint DEFAULT NULL,
  `address` text,
  `status` tinyint(1) DEFAULT NULL,
  `created` date DEFAULT (curdate())
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dump completed on 2026-02-19 15:10:05
