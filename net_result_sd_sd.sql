/*
Navicat MySQL Data Transfer

Source Server         : Server
Source Server Version : 50554
Source Host           : 172.26.253.3:3306
Source Database       : cyn_test

Target Server Type    : MYSQL
Target Server Version : 50554
File Encoding         : 65001

Date: 2017-06-18 18:02:43
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for net_result_sd_sd
-- ----------------------------
DROP TABLE IF EXISTS `net_result_sd_sd`;
CREATE TABLE `net_result_sd_sd` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `ip` varchar(50) NOT NULL DEFAULT '0',
  `date` date NOT NULL DEFAULT '0000-00-00',
  `time` time NOT NULL DEFAULT '00:00:00',
  `path_len` tinyint(4) DEFAULT NULL,
  `RTT` double(10,5) DEFAULT NULL,
  `delay_var` double(10,5) DEFAULT NULL,
  `packet_loss` tinyint(4) DEFAULT NULL,
  `province` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `operater` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22603 DEFAULT CHARSET=utf8;
