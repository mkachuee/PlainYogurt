-- MySQL dump 10.13  Distrib 5.7.16, for Linux (x86_64)
--
-- Host: localhost    Database: PYdatabase
-- ------------------------------------------------------
-- Server version	5.7.16-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add tree info',1,'add_treeinfo'),(2,'Can change tree info',1,'change_treeinfo'),(3,'Can delete tree info',1,'delete_treeinfo'),(4,'Can add subjects',2,'add_subjects'),(5,'Can change subjects',2,'change_subjects'),(6,'Can delete subjects',2,'delete_subjects'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add permission',5,'add_permission'),(14,'Can change permission',5,'change_permission'),(15,'Can delete permission',5,'delete_permission'),(16,'Can add content type',6,'add_contenttype'),(17,'Can change content type',6,'change_contenttype'),(18,'Can delete content type',6,'delete_contenttype'),(19,'Can add site',7,'add_site'),(20,'Can change site',7,'change_site'),(21,'Can delete site',7,'delete_site'),(22,'Can add session',8,'add_session'),(23,'Can change session',8,'change_session'),(24,'Can delete session',8,'delete_session'),(25,'Can add treeinfo',9,'add_treeinfo'),(26,'Can change treeinfo',9,'change_treeinfo'),(27,'Can delete treeinfo',9,'delete_treeinfo'),(28,'Can add subjects',10,'add_subjects'),(29,'Can change subjects',10,'change_subjects'),(30,'Can delete subjects',10,'delete_subjects'),(31,'Can add log entry',11,'add_logentry'),(32,'Can change log entry',11,'change_logentry'),(33,'Can delete log entry',11,'delete_logentry');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$30000$LSMnLz7HEqBK$K/18jagvLf41rGW8HSp+LU8QJtky8F5ecg/ewjsSAMQ=','2016-11-21 02:50:19.822175',1,'plainyogurt','','','sajad.d93@gmail.com',1,1,'2016-11-09 02:25:11.591357'),(2,'pbkdf2_sha256$30000$cP9L6kLKQuKn$eEYoju3DKTBj4ZqlUroNZ0+hAm+b3y4o7mlqH3747Fs=',NULL,1,'admin','','','admin@prerek.com',1,1,'2016-11-13 20:44:11.130151');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2016-11-13 21:31:34.558186','4','Aerospace Physics | Physics | Aerospace',1,'[{\"added\": {}}]',1,1),(2,'2016-11-13 21:32:20.522012','5','Algebra | Math | Algebra',1,'[{\"added\": {}}]',1,1),(3,'2016-11-13 21:33:36.034659','6','Deep Learning | Artificial Intillegence | Neural nets',1,'[{\"added\": {}}]',1,1),(4,'2016-11-13 21:34:47.964982','7','Machine Learning | Artificial Intillegence | Machine Learning',1,'[{\"added\": {}}]',1,1),(5,'2016-11-13 21:36:02.622682','8','Mechanics | Physics | FBD',1,'[{\"added\": {}}]',1,1),(6,'2016-11-20 06:55:38.746956','8','Mechanics | Physics | FBD',2,'[{\"changed\": {\"fields\": [\"DIRLink\"]}}]',1,1),(7,'2016-11-20 06:55:44.431688','7','Machine Learning | Artificial Intillegence | Machine Learning',2,'[{\"changed\": {\"fields\": [\"DIRLink\"]}}]',1,1),(8,'2016-11-20 06:55:50.968620','6','Deep Learning | Artificial Intillegence | Neural nets',2,'[{\"changed\": {\"fields\": [\"DIRLink\"]}}]',1,1),(9,'2016-11-20 06:55:57.602794','5','Algebra | Math | Algebra',2,'[{\"changed\": {\"fields\": [\"DIRLink\"]}}]',1,1),(10,'2016-11-20 06:56:03.796655','4','Aerospace Physics | Physics | Aerospace',2,'[{\"changed\": {\"fields\": [\"DIRLink\"]}}]',1,1),(11,'2016-11-20 18:24:55.010007','8','Mechanics | Physics | FBD',2,'[{\"changed\": {\"fields\": [\"DIRLink\"]}}]',1,1),(12,'2016-11-20 18:31:23.354289','7','Machine Learning | Artificial Intillegence | Machine Learning',2,'[{\"changed\": {\"fields\": [\"DIRLink\"]}}]',1,1),(13,'2016-11-20 18:31:29.311873','6','Deep Learning | Artificial Intillegence | Neural nets',2,'[{\"changed\": {\"fields\": [\"DIRLink\"]}}]',1,1),(14,'2016-11-20 18:31:34.274629','5','Algebra | Math | Algebra',2,'[{\"changed\": {\"fields\": [\"DIRLink\"]}}]',1,1),(15,'2016-11-20 18:31:39.350870','4','Aerospace Physics | Physics | Aerospace',2,'[{\"changed\": {\"fields\": [\"DIRLink\"]}}]',1,1),(16,'2016-11-20 18:34:28.252314','7','Machine Learning | Artificial Intillegence | Machine Learning',2,'[{\"changed\": {\"fields\": [\"DIRLink\"]}}]',1,1),(17,'2016-11-20 18:34:36.432389','6','Deep Learning | Artificial Intillegence | Neural nets',2,'[{\"changed\": {\"fields\": [\"DIRLink\"]}}]',1,1),(18,'2016-11-20 18:34:46.028085','4','Aerospace Physics | Physics | Aerospace',2,'[{\"changed\": {\"fields\": [\"DIRLink\"]}}]',1,1),(19,'2016-11-21 23:47:13.820250','10','Convolutional Neural Network | Machine Learning | CNN',2,'[{\"changed\": {\"fields\": [\"name\", \"DIRLink\"]}}]',1,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (11,'admin','logentry'),(3,'auth','group'),(5,'auth','permission'),(4,'auth','user'),(6,'contenttypes','contenttype'),(2,'home','subjects'),(1,'home','treeinfo'),(8,'sessions','session'),(7,'sites','site'),(10,'subjects','subjects'),(9,'subjects','treeinfo');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-10-29 20:53:40.258401'),(2,'contenttypes','0002_remove_content_type_name','2016-10-29 20:53:42.092073'),(3,'auth','0001_initial','2016-10-29 20:53:52.878200'),(4,'auth','0002_alter_permission_name_max_length','2016-10-29 20:53:53.038580'),(5,'auth','0003_alter_user_email_max_length','2016-10-29 20:53:53.330929'),(6,'auth','0004_alter_user_username_opts','2016-10-29 20:53:53.387668'),(7,'auth','0005_alter_user_last_login_null','2016-10-29 20:53:54.208775'),(8,'auth','0006_require_contenttypes_0002','2016-10-29 20:53:54.250314'),(9,'auth','0007_alter_validators_add_error_messages','2016-10-29 20:53:54.319729'),(10,'auth','0008_alter_user_username_max_length','2016-10-29 20:53:54.761179'),(12,'subjects','0001_initial','2016-10-29 20:53:57.341520'),(13,'subjects','0002_auto_20161029_1322','2016-10-29 20:53:57.715878'),(18,'sessions','0001_initial','2016-11-07 08:38:37.934552'),(19,'sites','0001_initial','2016-11-07 08:38:38.607361'),(20,'sites','0002_alter_domain_unique','2016-11-07 08:38:38.936282'),(21,'home','0001_initial','2016-11-07 18:06:28.218549'),(22,'home','0002_auto_20161107_1015','2016-11-07 18:15:37.647201'),(23,'admin','0001_initial','2016-11-09 02:31:35.946987'),(24,'admin','0002_logentry_remove_auto_add','2016-11-09 02:31:36.360653');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('jgfs8qmx5tyurzgpjtez3wc8o0nofymv','MGNlMjFhMTgzNTU1OWJmMWVjOTc3MjUyYTA3MmVmNmJmZjIzNTA1ODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzQwNmU1ZTU0YzJmNTFiOWQyYTJlNDA1MzUxMGI2Y2ZhODQyZjZkNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2016-12-05 02:50:19.923857'),('qpnrnqaoazl74k7rdbamaykn1zcrs2os','OWZlNDRkZWZlZTBiNWY0ZWI2MGQxYmEzYTI4OTY2MTMzOGQxNTEzODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3NDA2ZTVlNTRjMmY1MWI5ZDJhMmU0MDUzNTEwYjZjZmE4NDJmNmQ3In0=','2016-11-23 02:32:36.747532'),('rhutaitj1ba8e3etj7uwvu20viavhos5','YTA1Yzc5NmNkN2Q2ZjMzY2IxNmI4ZjRmNjQwMWZhOWNmMGU1YmMyMDp7Il9hdXRoX3VzZXJfaGFzaCI6Ijc0MDZlNWU1NGMyZjUxYjlkMmEyZTQwNTM1MTBiNmNmYTg0MmY2ZDciLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2016-12-04 06:55:16.105610');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_subjects`
--

DROP TABLE IF EXISTS `home_subjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_subjects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(200) NOT NULL,
  `subject` varchar(200) NOT NULL,
  `topic` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_subjects`
--

LOCK TABLES `home_subjects` WRITE;
/*!40000 ALTER TABLE `home_subjects` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_subjects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_treeinfo`
--

DROP TABLE IF EXISTS `home_treeinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_treeinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `topic` varchar(200) NOT NULL,
  `category` varchar(200) NOT NULL,
  `subject` varchar(200) NOT NULL,
  `DIRLink` varchar(200) NOT NULL,
  `tags` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_treeinfo`
--

LOCK TABLES `home_treeinfo` WRITE;
/*!40000 ALTER TABLE `home_treeinfo` DISABLE KEYS */;
INSERT INTO `home_treeinfo` VALUES (4,'Aerospace Physics','Dynamics and Controls','Physics','Aerospace','/TreeFiles/AerospacePhysics','aerospace physics dynamics controls'),(5,'Algebra','basics','Math','Algebra','/TreeFiles/Algebra','algebra division multiplication addition'),(6,'Deep Learning','deep neural networks','Artificial Intillegence','Neural nets','/TreeFiles/DeepLearning','neural nets learning ai artifical intillegence'),(7,'Machine Learning','classification regression','Artificial Intillegence','Machine Learning','/TreeFiles/MachineLearning','machine learning ai artificial intillgence'),(8,'Mechanics','Free Body Diagrams','Physics','FBD','/TreeFiles/Mechanics','free body diagram mechanics physics'),(9,'Math','multiplication','Math','Algebra','/TreeFiles/Math','multiplication, mult, add'),(10,'Convolutional Neural Network','CNN','Machine Learning','CNN','/TreeFiles/Convolutional Neural Network','learning');
/*!40000 ALTER TABLE `home_treeinfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-11-21 15:48:19
