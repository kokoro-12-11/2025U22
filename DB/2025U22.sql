-- MySQL dump 10.13  Distrib 9.1.0, for Win64 (x86_64)
--
-- Host: localhost    Database: 2025U22
-- ------------------------------------------------------
-- Server version	9.1.0

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
-- Table structure for table `answers`
--

DROP TABLE IF EXISTS `answers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `answers` (
  `answer_id` int NOT NULL AUTO_INCREMENT,
  `board_id` int NOT NULL,
  `user_id` int NOT NULL,
  `post_id` int NOT NULL,
  `answer_text` text NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`answer_id`),
  KEY `board_id` (`board_id`),
  KEY `user_id` (`user_id`),
  KEY `post_id` (`post_id`),
  CONSTRAINT `answers_ibfk_1` FOREIGN KEY (`board_id`) REFERENCES `boards` (`board_id`) ON DELETE CASCADE,
  CONSTRAINT `answers_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE,
  CONSTRAINT `answers_ibfk_3` FOREIGN KEY (`post_id`) REFERENCES `posts` (`post_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answers`
--

LOCK TABLES `answers` WRITE;
/*!40000 ALTER TABLE `answers` DISABLE KEYS */;
INSERT INTO `answers` VALUES (51,12,3,11,'今年は10月15日に実施予定です。詳しくは市のHPをご覧ください。','2025-08-20 19:35:53'),(52,13,4,12,'市役所の掲示板に案内が貼られていますよ。','2025-08-20 19:35:53'),(53,14,5,13,'町内イベントや清掃活動に使われているようです。','2025-08-20 19:35:53'),(54,15,6,14,'住民の推薦と多数決で決まっていたと思います。','2025-08-20 19:35:53'),(55,16,7,15,'今年も例年通り10月に開催されると聞いています。','2025-08-20 19:35:53'),(56,17,8,16,'ブランコの修理は来月予定されているそうです。','2025-08-20 19:35:53'),(57,18,9,17,'可燃ごみと不燃ごみの曜日が入れ替わったようです。','2025-08-20 19:35:53'),(58,19,10,18,'フンの始末や鳴き声に配慮してほしいです。','2025-08-20 19:35:53'),(59,20,11,19,'毎週水曜日の夜8時からです。','2025-08-20 19:35:53'),(60,21,12,20,'第1・第3木曜日に変更になったようです。','2025-08-20 19:35:53'),(61,12,3,11,'清掃活動は10月15日に予定されています。','2025-08-20 20:12:27'),(62,12,4,11,'来週の月曜に案内チラシが配布されます。','2025-08-20 20:12:27'),(63,12,5,11,'今年は地域で2回目の清掃を実施するそうです。','2025-08-20 20:12:27'),(64,12,6,11,'詳細は市のLINEアカウントにも掲載されていました。','2025-08-20 20:12:27'),(65,12,7,11,'9月末の自治会で正式に発表される予定です。','2025-08-20 20:12:27'),(66,12,8,11,'去年と同じく土曜日午前中に行うようです。','2025-08-20 20:12:27'),(67,12,9,11,'集会所前に集合してから清掃スタートになる予定です。','2025-08-20 20:12:27'),(68,12,10,11,'雨天の場合は翌週に延期されると聞いています。','2025-08-20 20:12:27'),(69,12,11,11,'当日は軍手とごみ袋を持参するよう案内されました。','2025-08-20 20:12:27'),(70,12,12,11,'回覧板にも記載があるので確認してみてください。','2025-08-20 20:12:27'),(71,27,16,26,'test','2025-08-25 07:58:14'),(72,27,16,26,'test2','2025-08-25 07:58:55'),(73,27,16,26,'testcvuw','2025-08-25 08:00:18'),(74,27,16,26,'12345','2025-08-25 08:07:09'),(75,27,16,26,'ｓぅや','2025-08-25 08:09:50'),(76,28,14,27,'ko','2025-08-25 09:06:42'),(77,28,14,27,'hi','2025-08-25 09:11:00'),(78,28,13,27,'cjwkn\r\n','2025-08-25 09:11:36'),(79,28,16,27,'njkds','2025-08-25 09:12:48'),(80,28,15,27,'dfg','2025-08-25 09:13:14'),(81,29,15,28,'test3\r\n','2025-08-25 09:16:02'),(82,29,13,28,'test1','2025-08-25 09:16:37'),(83,30,13,29,'cbhjsak','2025-08-25 09:20:00'),(84,31,16,30,'test','2025-08-25 14:11:05'),(85,31,13,30,'とりわきけいた','2025-08-25 14:12:16'),(86,32,14,31,'飯尾一成\r\n','2025-08-25 14:32:30'),(87,33,15,32,'山内\r\n','2025-08-25 14:36:46'),(88,34,13,33,'test1','2025-08-25 15:05:09');
/*!40000 ALTER TABLE `answers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `board_members`
--

DROP TABLE IF EXISTS `board_members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `board_members` (
  `board_id` int NOT NULL,
  `user_id` int NOT NULL,
  `role` enum('owner','editor','viewer') DEFAULT 'viewer',
  PRIMARY KEY (`board_id`,`user_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `board_members_ibfk_1` FOREIGN KEY (`board_id`) REFERENCES `boards` (`board_id`),
  CONSTRAINT `board_members_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `board_members`
--

LOCK TABLES `board_members` WRITE;
/*!40000 ALTER TABLE `board_members` DISABLE KEYS */;
/*!40000 ALTER TABLE `board_members` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `boards`
--

DROP TABLE IF EXISTS `boards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `boards` (
  `board_id` int NOT NULL AUTO_INCREMENT,
  `post_id` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `prefecture_id` int DEFAULT NULL,
  `send_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `is_skipped` tinyint(1) NOT NULL,
  `image_path` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`board_id`),
  KEY `fk_boards_prefecture` (`prefecture_id`),
  KEY `fk_boards_owner` (`user_id`),
  KEY `fk_boards_post` (`post_id`),
  CONSTRAINT `fk_boards_owner` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  CONSTRAINT `fk_boards_post` FOREIGN KEY (`post_id`) REFERENCES `posts` (`post_id`),
  CONSTRAINT `fk_boards_prefecture` FOREIGN KEY (`prefecture_id`) REFERENCES `prefectures` (`prefecture_id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `boards`
--

LOCK TABLES `boards` WRITE;
/*!40000 ALTER TABLE `boards` DISABLE KEYS */;
INSERT INTO `boards` VALUES (12,11,2,23,'2025-08-21 01:06:19',0,'static/boards/board_pref_23.png'),(13,12,2,13,'2025-08-21 01:06:19',0,'static/boards/board_pref_13.png'),(14,13,2,27,'2025-08-21 01:06:19',0,'static/boards/board_pref_27.png'),(15,14,2,12,'2025-08-21 01:06:19',0,'static/boards/board_pref_12.png'),(16,15,2,11,'2025-08-21 01:06:19',0,'static/boards/board_pref_11.png'),(17,16,2,28,'2025-08-21 01:06:19',0,'static/boards/board_pref_28.png'),(18,17,2,22,'2025-08-21 01:06:19',0,'static/boards/board_pref_22.png'),(19,18,2,40,'2025-08-21 01:06:19',0,'static/boards/board_pref_40.png'),(20,19,2,1,'2025-08-21 01:06:19',0,'static/boards/board_pref_1.png'),(21,20,2,46,'2025-08-21 01:06:19',0,'static/boards/board_pref_46.png'),(22,21,NULL,1,'2025-08-22 00:00:00',0,'static/boards/board_pref_1.png'),(23,22,NULL,47,'2025-08-22 00:00:00',0,'static/boards/board_pref_47.png'),(24,23,NULL,13,'2025-08-22 00:00:00',0,'static/boards/board_pref_13.png'),(25,24,NULL,13,'2025-08-22 00:00:00',0,'static/boards/board_pref_13.png'),(26,25,2,33,'2025-08-22 00:00:00',0,NULL),(27,26,2,47,'2025-08-25 00:00:00',0,'static/boards/board_pref_47.png'),(28,27,2,47,'2025-08-25 00:00:00',0,'static/boards/board_pref_47.png'),(29,28,2,47,'2025-08-25 00:00:00',0,'static/boards/board_pref_47.png'),(30,29,2,47,'2025-08-25 00:00:00',0,'static/boards/board_pref_47.png'),(31,30,2,47,'2025-08-25 00:00:00',0,'static/boards/board_pref_47.png'),(32,31,2,47,'2025-08-25 00:00:00',0,'static/boards/board_pref_47.png'),(33,32,2,47,'2025-08-25 00:00:00',0,'static/boards/board_pref_47.png'),(34,33,2,47,'2025-08-25 00:00:00',0,'static/boards/board_pref_47.png'),(35,34,2,47,'2025-08-25 00:00:00',0,'static/boards/board_pref_47.png');
/*!40000 ALTER TABLE `boards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `posts` (
  `post_id` int NOT NULL AUTO_INCREMENT,
  `board_id` int DEFAULT NULL,
  `prefecture_id` int DEFAULT NULL,
  `post_content` text,
  `ai_summary` text,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`post_id`),
  KEY `fk_posts_board` (`board_id`),
  CONSTRAINT `fk_posts_board` FOREIGN KEY (`board_id`) REFERENCES `boards` (`board_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES (11,12,23,'今年の地域清掃活動の日程を教えてください。',NULL,'2025-08-20 19:31:12'),(12,13,13,'防災訓練の詳細を知りたいです。',NULL,'2025-08-20 19:31:12'),(13,14,27,'町内会費の使い道について教えてください。',NULL,'2025-08-20 19:31:12'),(14,15,12,'自治会の役員はどのように決まりますか？',NULL,'2025-08-20 19:31:12'),(15,16,11,'今年のお祭りは開催されますか？',NULL,'2025-08-20 19:31:12'),(16,17,28,'公園の整備についての意見を募集しています。',NULL,'2025-08-20 19:31:12'),(17,18,22,'ゴミ出しルールの変更はありますか？',NULL,'2025-08-20 19:31:12'),(18,19,40,'ペット飼育に関するマナーについて意見をください。',NULL,'2025-08-20 19:31:12'),(19,20,1,'防犯パトロールはいつ実施されていますか？',NULL,'2025-08-20 19:31:12'),(20,21,46,'資源ゴミの回収日を教えてください。',NULL,'2025-08-20 19:31:12'),(21,NULL,1,'あなたの地元で一番おすすめの隠れた名所はどこですか？',NULL,'2025-08-22 00:17:04'),(22,NULL,47,'test',NULL,'2025-08-22 00:23:08'),(23,NULL,13,'あなたの地元で一番おすすめの隠れた名所はどこですか？',NULL,'2025-08-22 00:27:15'),(24,NULL,13,'あなたの地元で一番おすすめの隠れた名所はどこですか？',NULL,'2025-08-22 00:27:38'),(25,NULL,33,'test',NULL,'2025-08-22 14:33:39'),(26,NULL,47,'あなたの地元で一番おすすめの食べ物は何ですか？',NULL,'2025-08-25 07:08:54'),(27,NULL,47,'あなたの地元で、一番おすすめの隠れた名所はどこですか？',NULL,'2025-08-25 09:05:41'),(28,NULL,47,'test',NULL,'2025-08-25 09:14:45'),(29,NULL,47,'test1',NULL,'2025-08-25 09:19:05'),(30,NULL,47,'あなたの地元で一番おすすめの、地元の人しか知らない穴場スポットはどこですか？',NULL,'2025-08-25 14:10:00'),(31,NULL,47,'あなたの地元で一番おすすめの隠れた名所はどこですか？',NULL,'2025-08-25 14:20:35'),(32,NULL,47,'test',NULL,'2025-08-25 14:34:11'),(33,NULL,47,'test12345',NULL,'2025-08-25 15:04:25'),(34,35,47,'へちま',NULL,'2025-08-25 16:52:49');
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prefectures`
--

DROP TABLE IF EXISTS `prefectures`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prefectures` (
  `prefecture_id` int NOT NULL AUTO_INCREMENT,
  `prefecture_name` varchar(10) NOT NULL,
  PRIMARY KEY (`prefecture_id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prefectures`
--

LOCK TABLES `prefectures` WRITE;
/*!40000 ALTER TABLE `prefectures` DISABLE KEYS */;
INSERT INTO `prefectures` VALUES (1,'北海道'),(2,'青森県'),(3,'岩手県'),(4,'宮城県'),(5,'秋田県'),(6,'山形県'),(7,'福島県'),(8,'茨城県'),(9,'栃木県'),(10,'群馬県'),(11,'埼玉県'),(12,'千葉県'),(13,'東京都'),(14,'神奈川県'),(15,'新潟県'),(16,'富山県'),(17,'石川県'),(18,'福井県'),(19,'山梨県'),(20,'長野県'),(21,'岐阜県'),(22,'静岡県'),(23,'愛知県'),(24,'三重県'),(25,'滋賀県'),(26,'京都府'),(27,'大阪府'),(28,'兵庫県'),(29,'奈良県'),(30,'和歌山県'),(31,'鳥取県'),(32,'島根県'),(33,'岡山県'),(34,'広島県'),(35,'山口県'),(36,'徳島県'),(37,'香川県'),(38,'愛媛県'),(39,'高知県'),(40,'福岡県'),(41,'佐賀県'),(42,'長崎県'),(43,'熊本県'),(44,'大分県'),(45,'宮崎県'),(46,'鹿児島県'),(47,'沖縄県'),(48,'不明');
/*!40000 ALTER TABLE `prefectures` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(300) NOT NULL,
  `prefecture_id` int NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(50) DEFAULT 'member',
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email` (`email`),
  KEY `prefecture_id` (`prefecture_id`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`prefecture_id`) REFERENCES `prefectures` (`prefecture_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'board',10,'2025-08-17 02:40:20','2025-08-17 02:40:20',NULL,'board@icloud.com','scrypt:32768:8:1$QTvvuMeJUiVxKh76$7108bc7edab6484bd4b70ada157b2ec5a17311eb86afab6bb3f85e9e8cbe272252054e810cb968b4ad601ab4bdcdbbd5b015680a0c290b6f58ee54ed44105c62','member'),(2,'admin',23,'2025-08-20 17:19:57','2025-08-20 17:19:57',NULL,'admin@icloud.com','scrypt:32768:8:1$qUFZWZDkyjHrTmbA$2c8fc4e89c958093375129bd8b8bbc1634b6c12bdc1e98f1afa27217dfb5daf68d3b65af309f7acee90b5d8e8527e296ad16e296f6f186e69a5dd380df6fd781','admin'),(3,'user1',23,'2025-08-20 18:27:17','2025-08-20 18:27:17',NULL,'user1@example.com','pbkdf2:sha256:260000$UvNPMuVvFthAaLHF$ca678f263b4421c4f6d5e1ee7e6c878d0ec8c64e34a8d343c9ab6d871fa5b8c6','member'),(4,'user2',13,'2025-08-20 18:27:17','2025-08-20 18:27:17',NULL,'user2@example.com','pbkdf2:sha256:260000$UvNPMuVvFthAaLHF$ca678f263b4421c4f6d5e1ee7e6c878d0ec8c64e34a8d343c9ab6d871fa5b8c6','member'),(5,'user3',27,'2025-08-20 18:27:17','2025-08-20 18:27:17',NULL,'user3@example.com','pbkdf2:sha256:260000$UvNPMuVvFthAaLHF$ca678f263b4421c4f6d5e1ee7e6c878d0ec8c64e34a8d343c9ab6d871fa5b8c6','member'),(6,'user4',1,'2025-08-20 18:27:17','2025-08-20 18:27:17',NULL,'user4@example.com','pbkdf2:sha256:260000$UvNPMuVvFthAaLHF$ca678f263b4421c4f6d5e1ee7e6c878d0ec8c64e34a8d343c9ab6d871fa5b8c6','member'),(7,'user5',12,'2025-08-20 18:27:17','2025-08-20 18:27:17',NULL,'user5@example.com','pbkdf2:sha256:260000$UvNPMuVvFthAaLHF$ca678f263b4421c4f6d5e1ee7e6c878d0ec8c64e34a8d343c9ab6d871fa5b8c6','member'),(8,'user6',14,'2025-08-20 18:27:17','2025-08-20 18:27:17',NULL,'user6@example.com','pbkdf2:sha256:260000$UvNPMuVvFthAaLHF$ca678f263b4421c4f6d5e1ee7e6c878d0ec8c64e34a8d343c9ab6d871fa5b8c6','member'),(9,'user7',21,'2025-08-20 18:27:17','2025-08-20 18:27:17',NULL,'user7@example.com','pbkdf2:sha256:260000$UvNPMuVvFthAaLHF$ca678f263b4421c4f6d5e1ee7e6c878d0ec8c64e34a8d343c9ab6d871fa5b8c6','member'),(10,'user8',30,'2025-08-20 18:27:17','2025-08-20 18:27:17',NULL,'user8@example.com','pbkdf2:sha256:260000$UvNPMuVvFthAaLHF$ca678f263b4421c4f6d5e1ee7e6c878d0ec8c64e34a8d343c9ab6d871fa5b8c6','member'),(11,'user9',40,'2025-08-20 18:27:17','2025-08-20 18:27:17',NULL,'user9@example.com','pbkdf2:sha256:260000$UvNPMuVvFthAaLHF$ca678f263b4421c4f6d5e1ee7e6c878d0ec8c64e34a8d343c9ab6d871fa5b8c6','member'),(12,'user10',46,'2025-08-20 18:27:17','2025-08-20 18:27:17',NULL,'user10@example.com','pbkdf2:sha256:260000$UvNPMuVvFthAaLHF$ca678f263b4421c4f6d5e1ee7e6c878d0ec8c64e34a8d343c9ab6d871fa5b8c6','member'),(13,'test1',47,'2025-08-25 07:06:10','2025-08-25 07:06:10',NULL,'test1@test.com','scrypt:32768:8:1$tOJSR7a4llYX8DO6$21584491db01add20bc84877021c7f85439f5cf771083c9b16863370a7896b249d3548636149acad3e7f779249dfd0feb0702ba2813e3f7bb20a2543f4bd21b8','member'),(14,'test2',47,'2025-08-25 07:06:48','2025-08-25 07:06:48',NULL,'test2@test.com','scrypt:32768:8:1$UIUDkzpdTLbgUfYu$fb7a02e752c241a0a63fd5b9e84a64e7b59872a999a65b33ef24722994eaddf6be3b61ed72ae1156ef8b4d4393d3e5c43659879f5f40a96238ec5ecd1084fdf8','member'),(15,'test3',47,'2025-08-25 07:07:12','2025-08-25 07:07:12',NULL,'test3@test.com','scrypt:32768:8:1$FSbdD5EuCHDoEnRi$c80fb1baa62b216d79e57900840635385d4ae0d1d6b211fe0fe3fb9051b05d428dff9cb6ddd9e1c0866fb6402c8f294111a58e60659b4626711e6e899aeb5339','member'),(16,'test4',47,'2025-08-25 07:07:58','2025-08-25 07:07:58',NULL,'test4@test.com','scrypt:32768:8:1$M4pTdURQtuiQI6oL$97f53154a28cb1082727851ab730ab3affb30e2b4e5cf233242add17caa2d2fa6a662512a3453f887ea169814a77574f5cc8a737c9ee4e33f0ca458868055e4f','member'),(17,'test1',1,'2025-08-25 17:10:45','2025-08-25 17:10:45',NULL,'test1@icloud.com','scrypt:32768:8:1$fm5FC2Lk4NIBHweI$51d0c0a41ea4ac75a595f6e83c37a4d0d502f44ac074bfe4c0fc7dbecaf5f70d2795ce246783c93a24b8abb06cdc18432b227cdc4106ba6251cdb0609e7d6530','member');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `view_answers_by_prefecture`
--

DROP TABLE IF EXISTS `view_answers_by_prefecture`;
/*!50001 DROP VIEW IF EXISTS `view_answers_by_prefecture`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_answers_by_prefecture` AS SELECT 
 1 AS `prefecture_id`,
 1 AS `answer_text`,
 1 AS `created_at`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `view_answers_by_prefecture`
--

/*!50001 DROP VIEW IF EXISTS `view_answers_by_prefecture`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_answers_by_prefecture` AS select `p`.`prefecture_id` AS `prefecture_id`,`a`.`answer_text` AS `answer_text`,`a`.`created_at` AS `created_at` from (`answers` `a` join `posts` `p` on((`a`.`post_id` = `p`.`post_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-08-25 17:35:39
