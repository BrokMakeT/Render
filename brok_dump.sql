-- MySQL dump 10.13  Distrib 8.0.39, for Win64 (x86_64)
--
-- Host: localhost    Database: brok
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Current Database: `brok`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `brok` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `brok`;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add cliente',7,'add_cliente'),(26,'Can change cliente',7,'change_cliente'),(27,'Can delete cliente',7,'delete_cliente'),(28,'Can view cliente',7,'view_cliente'),(29,'Can add salario',8,'add_salario'),(30,'Can change salario',8,'change_salario'),(31,'Can delete salario',8,'delete_salario'),(32,'Can view salario',8,'view_salario'),(33,'Can add mensaje whats app',9,'add_mensajewhatsapp'),(34,'Can change mensaje whats app',9,'change_mensajewhatsapp'),(35,'Can delete mensaje whats app',9,'delete_mensajewhatsapp'),(36,'Can view mensaje whats app',9,'view_mensajewhatsapp'),(37,'Can add tarea',10,'add_tarea'),(38,'Can change tarea',10,'change_tarea'),(39,'Can delete tarea',10,'delete_tarea'),(40,'Can view tarea',10,'view_tarea'),(41,'Can add cotizacion',11,'add_cotizacion'),(42,'Can change cotizacion',11,'change_cotizacion'),(43,'Can delete cotizacion',11,'delete_cotizacion'),(44,'Can view cotizacion',11,'view_cotizacion'),(45,'Can add usuario',12,'add_usuario'),(46,'Can change usuario',12,'change_usuario'),(47,'Can delete usuario',12,'delete_usuario'),(48,'Can view usuario',12,'view_usuario'),(49,'Can add notificacion',13,'add_notificacion'),(50,'Can change notificacion',13,'change_notificacion'),(51,'Can delete notificacion',13,'delete_notificacion'),(52,'Can view notificacion',13,'view_notificacion'),(53,'Can add factura',14,'add_factura'),(54,'Can change factura',14,'change_factura'),(55,'Can delete factura',14,'delete_factura'),(56,'Can view factura',14,'view_factura');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$870000$UIcUgBQkIxMLByPfNG2k0U$PaObRYI4uRJ/wSbeLgWqvEXXeVaSWVk/no/FLolAlZA=','2024-10-04 23:57:35.551031',1,'admin','','','admin@gmail.com',1,1,'2024-10-04 23:56:32.780304');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brokeapp_cliente`
--

DROP TABLE IF EXISTS `brokeapp_cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brokeapp_cliente` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre_empresa` varchar(100) NOT NULL,
  `contacto_nombre` varchar(100) NOT NULL,
  `contacto_email` varchar(254) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `direccion` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brokeapp_cliente`
--

LOCK TABLES `brokeapp_cliente` WRITE;
/*!40000 ALTER TABLE `brokeapp_cliente` DISABLE KEYS */;
/*!40000 ALTER TABLE `brokeapp_cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brokeapp_cotizacion`
--

DROP TABLE IF EXISTS `brokeapp_cotizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brokeapp_cotizacion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `estado` varchar(50) NOT NULL,
  `cliente_id` bigint NOT NULL,
  `usuario_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `brokeAPP_cotizacion_cliente_id_68837d52_fk_brokeAPP_cliente_id` (`cliente_id`),
  KEY `brokeAPP_cotizacion_usuario_id_0b0bc885_fk_brokeAPP_usuario_id` (`usuario_id`),
  CONSTRAINT `brokeAPP_cotizacion_cliente_id_68837d52_fk_brokeAPP_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `brokeapp_cliente` (`id`),
  CONSTRAINT `brokeAPP_cotizacion_usuario_id_0b0bc885_fk_brokeAPP_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `brokeapp_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brokeapp_cotizacion`
--

LOCK TABLES `brokeapp_cotizacion` WRITE;
/*!40000 ALTER TABLE `brokeapp_cotizacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `brokeapp_cotizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brokeapp_factura`
--

DROP TABLE IF EXISTS `brokeapp_factura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brokeapp_factura` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `pagada` tinyint(1) NOT NULL,
  `cotizacion_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `brokeAPP_factura_cotizacion_id_dd8c9430_fk_brokeAPP_` (`cotizacion_id`),
  CONSTRAINT `brokeAPP_factura_cotizacion_id_dd8c9430_fk_brokeAPP_` FOREIGN KEY (`cotizacion_id`) REFERENCES `brokeapp_cotizacion` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brokeapp_factura`
--

LOCK TABLES `brokeapp_factura` WRITE;
/*!40000 ALTER TABLE `brokeapp_factura` DISABLE KEYS */;
/*!40000 ALTER TABLE `brokeapp_factura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brokeapp_mensajewhatsapp`
--

DROP TABLE IF EXISTS `brokeapp_mensajewhatsapp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brokeapp_mensajewhatsapp` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `mensaje` longtext NOT NULL,
  `imagen_url` varchar(255) NOT NULL,
  `fecha_envio` datetime(6) NOT NULL,
  `usuario_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `brokeAPP_mensajewhat_usuario_id_fce4ea3d_fk_brokeAPP_` (`usuario_id`),
  CONSTRAINT `brokeAPP_mensajewhat_usuario_id_fce4ea3d_fk_brokeAPP_` FOREIGN KEY (`usuario_id`) REFERENCES `brokeapp_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brokeapp_mensajewhatsapp`
--

LOCK TABLES `brokeapp_mensajewhatsapp` WRITE;
/*!40000 ALTER TABLE `brokeapp_mensajewhatsapp` DISABLE KEYS */;
/*!40000 ALTER TABLE `brokeapp_mensajewhatsapp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brokeapp_notificacion`
--

DROP TABLE IF EXISTS `brokeapp_notificacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brokeapp_notificacion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tipo` varchar(20) NOT NULL,
  `descripcion` longtext NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `leida` tinyint(1) NOT NULL,
  `usuario_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `brokeAPP_notificacion_usuario_id_b6bc20c0_fk_brokeAPP_usuario_id` (`usuario_id`),
  CONSTRAINT `brokeAPP_notificacion_usuario_id_b6bc20c0_fk_brokeAPP_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `brokeapp_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brokeapp_notificacion`
--

LOCK TABLES `brokeapp_notificacion` WRITE;
/*!40000 ALTER TABLE `brokeapp_notificacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `brokeapp_notificacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brokeapp_salario`
--

DROP TABLE IF EXISTS `brokeapp_salario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brokeapp_salario` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `lugar_trabajo` varchar(100) NOT NULL,
  `viaticos` decimal(10,2) NOT NULL,
  `pago_actividad` decimal(10,2) NOT NULL,
  `total_pago` decimal(10,2) NOT NULL,
  `fecha_pago` date NOT NULL,
  `tarea_id` bigint NOT NULL,
  `usuario_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `brokeAPP_salario_tarea_id_2654ac58_fk_brokeAPP_tarea_id` (`tarea_id`),
  KEY `brokeAPP_salario_usuario_id_d3f74879_fk_brokeAPP_usuario_id` (`usuario_id`),
  CONSTRAINT `brokeAPP_salario_tarea_id_2654ac58_fk_brokeAPP_tarea_id` FOREIGN KEY (`tarea_id`) REFERENCES `brokeapp_tarea` (`id`),
  CONSTRAINT `brokeAPP_salario_usuario_id_d3f74879_fk_brokeAPP_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `brokeapp_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brokeapp_salario`
--

LOCK TABLES `brokeapp_salario` WRITE;
/*!40000 ALTER TABLE `brokeapp_salario` DISABLE KEYS */;
/*!40000 ALTER TABLE `brokeapp_salario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brokeapp_tarea`
--

DROP TABLE IF EXISTS `brokeapp_tarea`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brokeapp_tarea` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `descripcion` longtext NOT NULL,
  `fecha_asignacion` datetime(6) NOT NULL,
  `fecha_vencimiento` date DEFAULT NULL,
  `estado` varchar(50) NOT NULL,
  `usuario_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `brokeAPP_tarea_usuario_id_7d2cb20d_fk_brokeAPP_usuario_id` (`usuario_id`),
  CONSTRAINT `brokeAPP_tarea_usuario_id_7d2cb20d_fk_brokeAPP_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `brokeapp_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brokeapp_tarea`
--

LOCK TABLES `brokeapp_tarea` WRITE;
/*!40000 ALTER TABLE `brokeapp_tarea` DISABLE KEYS */;
/*!40000 ALTER TABLE `brokeapp_tarea` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brokeapp_usuario`
--

DROP TABLE IF EXISTS `brokeapp_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brokeapp_usuario` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `rol` varchar(10) NOT NULL,
  `contrasena` varchar(255) NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `brokeAPP_usuario_email_ecff2a8a_uniq` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brokeapp_usuario`
--

LOCK TABLES `brokeapp_usuario` WRITE;
/*!40000 ALTER TABLE `brokeapp_usuario` DISABLE KEYS */;
INSERT INTO `brokeapp_usuario` VALUES (2,'samuel','nunez','samuel@gmail.com','5525409827','Admin','123','2024-10-07 21:53:49.129223'),(3,'Gael','Castellanos','Gael@gmail.com','5525555555555','Admin','12345','2024-10-07 21:55:42.299207'),(4,'pepe','benito','pepe@gmail.com','552555555','Empleado','123','2024-10-07 22:04:59.408728'),(5,'juan','caca','juan@gmail.com','552555555','Empleado','333','2024-10-07 22:06:19.433653'),(12,'Gael','Castellanos','j@gmail.com','5525555555555','Empleado','123','2024-10-07 22:25:31.616704'),(13,'Gael','Castellanos','pepe22@gmail.com','5525409827','Empleado','123','2024-10-07 22:29:17.950191'),(14,'ricardo','benito','robin@gmail.com','5525409827','Empleado','123','2024-10-08 00:12:05.427955');
/*!40000 ALTER TABLE `brokeapp_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(7,'brokeAPP','cliente'),(11,'brokeAPP','cotizacion'),(14,'brokeAPP','factura'),(9,'brokeAPP','mensajewhatsapp'),(13,'brokeAPP','notificacion'),(8,'brokeAPP','salario'),(10,'brokeAPP','tarea'),(12,'brokeAPP','usuario'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-10-02 23:04:35.044544'),(2,'auth','0001_initial','2024-10-02 23:04:35.410683'),(3,'admin','0001_initial','2024-10-02 23:04:35.499909'),(4,'admin','0002_logentry_remove_auto_add','2024-10-02 23:04:35.504914'),(5,'admin','0003_logentry_add_action_flag_choices','2024-10-02 23:04:35.509918'),(6,'contenttypes','0002_remove_content_type_name','2024-10-02 23:04:35.582225'),(7,'auth','0002_alter_permission_name_max_length','2024-10-02 23:04:35.630245'),(8,'auth','0003_alter_user_email_max_length','2024-10-02 23:04:35.645259'),(9,'auth','0004_alter_user_username_opts','2024-10-02 23:04:35.651264'),(10,'auth','0005_alter_user_last_login_null','2024-10-02 23:04:35.702311'),(11,'auth','0006_require_contenttypes_0002','2024-10-02 23:04:35.704312'),(12,'auth','0007_alter_validators_add_error_messages','2024-10-02 23:04:35.709317'),(13,'auth','0008_alter_user_username_max_length','2024-10-02 23:04:35.761364'),(14,'auth','0009_alter_user_last_name_max_length','2024-10-02 23:04:35.811410'),(15,'auth','0010_alter_group_name_max_length','2024-10-02 23:04:35.824422'),(16,'auth','0011_update_proxy_permissions','2024-10-02 23:04:35.829426'),(17,'auth','0012_alter_user_first_name_max_length','2024-10-02 23:04:35.878471'),(18,'sessions','0001_initial','2024-10-02 23:04:35.899490'),(19,'brokeAPP','0001_initial','2024-10-04 22:01:58.458489'),(20,'brokeAPP','0002_alter_usuario_contrasena_alter_usuario_email_and_more','2024-10-05 00:22:49.434765'),(21,'brokeAPP','0003_alter_usuario_contrasena_alter_usuario_email_and_more','2024-10-05 00:25:24.234498');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('3bt4xj3g19vq9sgrm2tryw9ftj31mr1j','.eJxVjEsOwiAUAO_C2pA-_rh03zOQxwOkamhS2pXx7oakC93OTObNAh57DUfPW1gSuzJgl18WkZ65DZEe2O4rp7Xt2xL5SPhpO5_XlF-3s_0bVOx1bBV4XTQhWQKTYwIsXrgEsXhJSiuIjpyNWrokhVZopUGhJUymGG8n9vkC5UE3Qw:1swsAx:e8GTz2zQKPhWySQMWX3W5Ku9_tcwp1xe0vrxE8Ib2H0','2024-10-18 23:57:35.552033');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-07 18:12:38
