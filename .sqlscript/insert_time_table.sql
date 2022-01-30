-- Using .sql script in LINUX terminal :-
-----------------------------------------
-- mysql -u root -p salahtimetable
-- source /docker-entrypoint-initdb.d/1_insert_time_table.sql



-- Testing data insertion using any MySQL client :-
---------------------------------------------------
-- create database salahtimetable;
-- use salahtimetable;
-- create table january_table (date_pk int primary key, sehri_ends varchar(10), fajr_starts varchar(10), fajr_ends varchar(10), duhur_starts varchar(10), duhur_ends varchar(10), asr_starts varchar(10), asr_ends varchar(10), maghrib_starts varchar(10), maghrib_ends varchar(10), isha_starts varchar(10), isha_ends varchar(10), makrooh_morning_starts varchar(10), makrooh_morning_ends varchar(10), makrooh_noon_starts varchar(10), makrooh_noon_ends varchar(10), makrooh_evening_starts varchar(10), makrooh_evening_ends varchar(10));
-- INSERT IGNORE INTO january_table (date_pk, sehri_ends, fajr_starts, fajr_ends, duhur_starts, duhur_ends, asr_starts, asr_ends, maghrib_starts, maghrib_ends, isha_starts, isha_ends, makrooh_morning_starts, makrooh_morning_ends, makrooh_noon_starts, makrooh_noon_ends, makrooh_evening_starts, makrooh_evening_ends) VALUES
-- (1,"4:51 AM","4:57 AM","6:16 AM","11:41 AM","3:26 PM","3:27 PM","5:03 PM","5:08 PM","6:22 PM","6:23 PM","","6:16 AM","6:36 AM","10:59 AM","11:40 AM","4:43 PM","5:03 PM");



-- January Time Table
INSERT IGNORE INTO january_table (makrooh_evening_ends, makrooh_evening_starts, makrooh_noon_ends, makrooh_noon_starts, makrooh_morning_ends, makrooh_morning_starts, isha_ends, isha_starts, maghrib_ends, maghrib_starts, asr_ends, asr_starts, duhur_ends, duhur_starts, fajr_ends, fajr_starts, sehri_ends, date_pk) VALUES
("5:03 PM", "4:43 PM", "11:40 AM", "10:59 AM", "6:36 AM", "6:16 AM", "", "6:23 PM", "6:22 PM", "5:08 PM", "5:03 PM", "3:27 PM", "3:26 PM", "11:41 AM", "6:16 AM", "4:57 AM", "4:51 AM", 1),
("5:04 PM", "4:44 PM", "11:40 AM", "11:00 AM", "6:37 AM", "6:17 AM", "", "6:24 PM", "6:23 PM", "5:09 PM", "5:04 PM", "3:28 PM", "3:27 PM", "11:41 AM", "6:17 AM", "4:57 AM", "4:51 AM", 2),
("5:04 PM", "4:44 PM", "11:41 AM", "11:00 AM", "6:37 AM", "6:17 AM", "", "6:24 PM", "6:23 PM", "5:09 PM", "5:04 PM", "3:29 PM", "3:28 PM", "11:42 AM", "6:17 AM", "4:57 AM", "4:51 AM", 3),
("5:05 PM", "4:45 PM", "11:41 AM", "11:01 AM", "6:37 AM", "6:17 AM", "", "6:25 PM", "6:24 PM", "5:10 PM", "5:05 PM", "3:29 PM", "3:28 PM", "11:42 AM", "6:17 AM", "4:58 AM", "4:52 AM", 4),
("5:06 PM", "4:46 PM", "11:42 AM", "11:01 AM", "6:38 AM", "6:18 AM", "", "6:25 PM", "6:24 PM", "5:11 PM", "5:06 PM", "3:30 PM", "3:29 PM", "11:43 AM", "6:18 AM", "4:58 AM", "4:52 AM", 5),
("5:06 PM", "4:46 PM", "11:42 AM", "11:02 AM", "6:38 AM", "6:18 AM", "", "6:26 PM", "6:25 PM", "5:11 PM", "5:06 PM", "3:31 PM", "3:30 PM", "11:43 AM", "6:18 AM", "4:58 AM", "4:52 AM", 6),
("5:07 PM", "4:47 PM", "11:43 AM", "11:02 AM", "6 38 AM", "6:18 AM", "", "6:27 PM", "6:26 PM", "5:12 PM", "5:07 PM", "3:31 PM", "3:30 PM", "11:44 AM", "6:18 AM", "4:58 AM", "4:52 AM", 7),
("5:08 PM", "4:48 PM", "11:43 AM", "11:03 AM", "6:38 AM", "6:18 AM", "", "6:27 PM", "6:26 PM", "5:13 PM", "5:08 PM", "3:32 PM", "3:31 PM", "11:44 AM", "6:18 AM", "4:59 AM", "4:53 AM", 8),
("5:08 PM", "4:48 PM", "11:43 AM", "11:03 AM", "6:38 AM", "6:18 AM", "", "6:28 PM", "6:27 PM", "5:13 PM", "5:08 PM", "3:33 PM", "3:32 PM", "11:44 AM", "6:18 AM", "4:59 AM", "4:53 AM", 9),
("5:09 PM", "4:49 PM", "11:44 AM", "11:04 AM", "6:38 AM", "6:18 AM", "", "6:29 PM", "6:28 PM", "5:14 PM", "5:09 PM", "3:33 PM", "3:32 PM", "11:45 AM", "6:18 AM", "4:59 AM", "4:53 AM", 10),
("5:10 PM", "4:50 PM", "11:44 AM", "11:04 AM", "6:39 AM", "6:19 AM", "", "6:29 PM", "6:28 PM", "5:15 PM", "5:10 PM", "3:34 PM", "3:33 PM", "11:45 AM", "6:19 AM", "4:59 AM", "4:53 AM", 11),
("5:10 PM", "4:50 PM", "11:45 AM", "11:05 AM", "6:39 AM", "6:19 AM", "", "6:30 PM", "6:29 PM", "5:15 PM", "5:10 PM", "3:35 PM", "3:34 PM", "11:46 AM", "6:19 AM", "5:00 AM", "4:54 AM", 12),
("5:11 PM", "4:51 PM", "11:45 AM", "11:05 AM", "6:39 AM", "6:19 AM", "", "6:30 PM", "6:29 PM", "5:16 PM", "5:11 PM", "3:36 PM", "3:35 PM", "11:46 AM", "6:19 AM", "5:00 AM", "4:54 AM", 13),
("5:12 PM", "4:52 PM", "11:45 AM", "11:06 AM", "6:39 AM", "6:19 AM", "", "6:31 PM", "6:30 PM", "5:17 PM", "5:12 PM", "3:36 PM", "3:35 PM", "11:46 AM", "6:19 AM", "5:00 AM", "4:54 AM", 14),
("5:13 PM", "4:53 PM", "11:46 AM", "11:06 AM", "6:39 AM", "6:19 AM", "", "6:31 PM", "6:30 PM", "5:18 PM", "5:13 PM", "3:37 PM", "3:36 PM", "11:47 AM", "6:19 AM", "5:00 AM", "4:54 AM", 15),
("5:13 PM", "4:53 PM", "11:46 AM", "11:07 AM", "6:39 AM", "6:19 AM", "", "6:32 PM", "6:31 PM", "5:18 PM", "5:13 PM", "3:38 PM", "3:37 PM", "11:47 AM", "6:19 AM", "5:00 AM", "4:54 AM", 16),
("5:14 PM", "4:54 PM", "11:46 AM", "11:07 AM", "6:39 AM", "6:19 AM", "", "6:33 PM", "6:32 PM", "5:19 PM", "5:14 PM", "3:38 PM", "3:37 PM", "11:47 AM", "6:19 AM", "5:00 AM", "4:54 AM", 17),
("5:15 PM", "4:55 PM", "11:47 AM", "11:07 AM", "6:39 AM", "6:19 AM", "", "6:33 PM", "6:32 PM", "5:20 PM", "5:15 PM", "3:39 PM", "3:38 PM", "11:48 AM", "6:19 AM", "5:00 AM", "4:54 AM", 18),
("5:16 PM", "4:56 PM", "11:47 AM", "11:08 AM", "6:39 AM", "6:19 AM", "", "6:34 PM", "6:33 PM", "5:21 PM", "5:16 PM", "3:40 PM", "3:39 PM", "11:48 AM", "6:19 AM", "5:00 AM", "4:54 AM", 19),
("5:16 PM", "4:56 PM", "11:47 AM", "11:08 AM", "6:38 AM", "6:18 AM", "", "6:34 PM", "6:33 PM", "5:21 PM", "5:16 PM", "3:41 PM", "3:40 PM", "11:49 AM", "6:18 AM", "5:00 AM", "4:54 AM", 20),
("5:17 PM", "4:57 PM", "11:48 AM", "11:08 AM", "6:38 AM", "6:18 AM", "", "6:35 PM", "6:34 PM", "5:22 PM", "5:17 PM", "3:41 PM", "3:40 PM", "11:49 AM", "6:18 AM", "5:00 AM", "4:54 AM", 21),
("5:18 PM", "4:58 PM", "11:48 AM", "11:09 AM", "6:38 AM", "6:18 AM", "", "6:36 PM", "6:35 PM", "5:23 PM", "5:18 PM", "3:42 PM", "3:41 PM", "11:49 AM", "6:18 AM", "5:00 AM", "4:54 AM", 22),
("5:18 PM", "4:58 PM", "11:48 AM", "11:09 AM", "6:38 AM", "6:18 AM", "", "6:36 PM", "6:35 PM", "5:23 PM", "5:18 PM", "3:43 PM", "3:42 PM", "11:49 AM", "6:18 AM", "5:00 AM", "4:54 AM", 23),
("5:19 PM", "4:59 PM", "11:49 AM", "11:09 AM", "6:38 AM", "6:18 AM", "", "6:37 PM", "6:36 PM", "5:24 PM", "5:19 PM", "3:43 PM", "3:42 PM", "11:50 AM", "6:18 AM", "5:00 AM", "4:54 AM", 24),
("5:20 PM", "5:00 PM", "11:49 AM", "11:09 AM", "6:38 AM", "6:18 AM", "", "6:37 PM", "6:36 PM", "5:25 PM", "5:20 PM", "3:44 PM", "3:43 PM", "11:50 AM", "6:18 AM", "5:00 AM", "4:54 AM", 25),
("5:20 PM", "5:00 PM", "11:49 AM", "11:10 AM", "6:37 AM", "6:17 AM", "", "6:38 PM", "6:37 PM", "5:25 PM", "5:20 PM", "3:45 PM", "3:44 PM", "11:50 AM", "6:17 AM", "5:00 AM", "4:54 AM", 26),
("5:21 PM", "5:01 PM", "11:49 AM", "11:10 AM", "6:37 AM", "6:17 AM", "", "6:39 PM", "6:38 PM", "5:26 PM", "5:21 PM", "3:45 PM", "3:44 PM", "11:50 AM", "6:17 AM", "5:00 AM", "4:54 AM", 27),
("5:22 PM", "5:02 PM", "11:49 AM", "11:10 AM", "6:37 AM", "6:17 AM", "", "6:39 PM", "6:38 PM", "5:27 PM", "5:22 PM", "3:46 PM", "3:45 PM", "11:50 AM", "6:17 AM", "5:00 AM", "4:54 AM", 28),
("5:22 PM", "5:02 PM", "11:50 AM", "11:10 AM", "6:37 AM", "6:17 AM", "", "6:40 PM", "6:39 PM", "5:27 PM", "5:22 PM", "3:47 PM", "3:46 PM", "11:51 AM", "6:17 AM", "4:59 AM", "4:53 AM", 29),
("5:23 PM", "5:03 PM", "11:50 AM", "11:11 AM", "6:36 AM", "6:16 AM", "", "6:40 PM", "6:39 PM", "5:28 PM", "5:23 PM", "3:47 PM", "3:46 PM", "11:51 AM", "6:16 AM", "4:59 AM", "4:53 AM", 30),
("5:24 PM", "5:04 PM", "11:50 AM", "11:11 AM", "6:36 AM", "6:16 AM", "", "6:41 PM", "6:40 PM", "5:29 PM", "5:24 PM", "3:47 PM", "3:46 PM", "11:51 AM", "6:16 AM", "4:59 AM", "4:53 AM", 31);




