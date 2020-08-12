/*
Navicat MySQL Data Transfer

Source Server         : 服务器
Source Server Version : 50647
Source Host           : 121.36.253.244:3306
Source Database       : houseprice

Target Server Type    : MYSQL
Target Server Version : 50647
File Encoding         : 65001

Date: 2020-08-11 21:48:17
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `alembic_version`
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('4cddf371c79e');

-- ----------------------------
-- Table structure for `blacklist`
-- ----------------------------
DROP TABLE IF EXISTS `blacklist`;
CREATE TABLE `blacklist` (
  `user_id` int(11) DEFAULT NULL,
  `block_id` int(11) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  KEY `fk_blacklist_block_id_users` (`block_id`),
  KEY `fk_blacklist_user_id_users` (`user_id`),
  CONSTRAINT `fk_blacklist_block_id_users` FOREIGN KEY (`block_id`) REFERENCES `users` (`id`),
  CONSTRAINT `fk_blacklist_user_id_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of blacklist
-- ----------------------------
INSERT INTO `blacklist` VALUES ('2', '4', '2020-08-08 14:31:57');

-- ----------------------------
-- Table structure for `comments`
-- ----------------------------
DROP TABLE IF EXISTS `comments`;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `body` text,
  `timestamp` datetime DEFAULT NULL,
  `mark_read` tinyint(1) DEFAULT NULL,
  `disabled` tinyint(1) DEFAULT NULL,
  `author_id` int(11) DEFAULT NULL,
  `post_id` int(11) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_comments_post_id_posts` (`post_id`),
  KEY `fk_comments_parent_id_comments` (`parent_id`),
  KEY `fk_comments_author_id_users` (`author_id`),
  KEY `ix_comments_timestamp` (`timestamp`),
  CONSTRAINT `fk_comments_author_id_users` FOREIGN KEY (`author_id`) REFERENCES `users` (`id`),
  CONSTRAINT `fk_comments_parent_id_comments` FOREIGN KEY (`parent_id`) REFERENCES `comments` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_comments_post_id_posts` FOREIGN KEY (`post_id`) REFERENCES `posts` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of comments
-- ----------------------------
INSERT INTO `comments` VALUES ('1', 'test', '2020-08-11 12:02:29', '0', '0', '8', '8', null);
INSERT INTO `comments` VALUES ('2', '<a href=\"/user/8\" class=\"g-text-underline--none--hover\">@汪志豪 </a>123', '2020-08-11 12:08:38', '0', '0', '10', '8', '1');
INSERT INTO `comments` VALUES ('4', 'test', '2020-08-11 12:20:52', '0', '0', '8', '7', null);

-- ----------------------------
-- Table structure for `comments_likes`
-- ----------------------------
DROP TABLE IF EXISTS `comments_likes`;
CREATE TABLE `comments_likes` (
  `user_id` int(11) DEFAULT NULL,
  `comment_id` int(11) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  KEY `fk_comments_likes_comment_id_comments` (`comment_id`),
  KEY `fk_comments_likes_user_id_users` (`user_id`),
  CONSTRAINT `fk_comments_likes_comment_id_comments` FOREIGN KEY (`comment_id`) REFERENCES `comments` (`id`),
  CONSTRAINT `fk_comments_likes_user_id_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of comments_likes
-- ----------------------------
INSERT INTO `comments_likes` VALUES ('10', '1', '2020-08-11 12:08:31');
INSERT INTO `comments_likes` VALUES ('10', '2', '2020-08-11 12:16:17');
INSERT INTO `comments_likes` VALUES ('8', '2', '2020-08-11 12:19:51');
INSERT INTO `comments_likes` VALUES ('8', '4', '2020-08-11 12:20:55');
INSERT INTO `comments_likes` VALUES ('8', '1', '2020-08-11 13:13:47');

-- ----------------------------
-- Table structure for `followers`
-- ----------------------------
DROP TABLE IF EXISTS `followers`;
CREATE TABLE `followers` (
  `follower_id` int(11) DEFAULT NULL,
  `followed_id` int(11) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  KEY `follower_id` (`follower_id`),
  KEY `followed_id` (`followed_id`),
  CONSTRAINT `followers_ibfk_1` FOREIGN KEY (`follower_id`) REFERENCES `users` (`id`),
  CONSTRAINT `followers_ibfk_2` FOREIGN KEY (`followed_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of followers
-- ----------------------------

-- ----------------------------
-- Table structure for `messages`
-- ----------------------------
DROP TABLE IF EXISTS `messages`;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `body` text,
  `timestamp` datetime DEFAULT NULL,
  `sender_id` int(11) DEFAULT NULL,
  `recipient_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_messages_sender_id_users` (`sender_id`),
  KEY `fk_messages_recipient_id_users` (`recipient_id`),
  KEY `ix_messages_timestamp` (`timestamp`),
  CONSTRAINT `fk_messages_recipient_id_users` FOREIGN KEY (`recipient_id`) REFERENCES `users` (`id`),
  CONSTRAINT `fk_messages_sender_id_users` FOREIGN KEY (`sender_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of messages
-- ----------------------------
INSERT INTO `messages` VALUES ('6', '1', '2020-08-08 14:29:18', '4', '2');
INSERT INTO `messages` VALUES ('7', '2', '2020-08-08 14:29:20', '4', '2');
INSERT INTO `messages` VALUES ('8', '3', '2020-08-08 14:29:25', '4', '2');
INSERT INTO `messages` VALUES ('9', '4', '2020-08-08 14:29:28', '4', '2');
INSERT INTO `messages` VALUES ('10', '5', '2020-08-08 14:30:59', '4', '2');
INSERT INTO `messages` VALUES ('11', '6', '2020-08-08 14:31:02', '4', '2');
INSERT INTO `messages` VALUES ('12', 'gun', '2020-08-08 14:32:07', '2', '4');
INSERT INTO `messages` VALUES ('13', 'hello', '2020-08-09 14:53:25', '7', '2');
INSERT INTO `messages` VALUES ('14', '123', '2020-08-11 12:07:08', '10', '8');

-- ----------------------------
-- Table structure for `notifications`
-- ----------------------------
DROP TABLE IF EXISTS `notifications`;
CREATE TABLE `notifications` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `timestamp` float DEFAULT NULL,
  `payload_json` text,
  PRIMARY KEY (`id`),
  KEY `fk_notifications_user_id_users` (`user_id`),
  KEY `ix_notifications_name` (`name`),
  KEY `ix_notifications_timestamp` (`timestamp`),
  CONSTRAINT `fk_notifications_user_id_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=113 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of notifications
-- ----------------------------
INSERT INTO `notifications` VALUES ('5', 'unread_recived_comments_count', '3', '1596880000', '0');
INSERT INTO `notifications` VALUES ('11', 'unread_likes_count', '2', '1596880000', '0');
INSERT INTO `notifications` VALUES ('20', 'unread_likes_count', '4', '1596900000', '0');
INSERT INTO `notifications` VALUES ('25', 'unread_follows_count', '2', '1596900000', '0');
INSERT INTO `notifications` VALUES ('30', 'unread_messages_count', '4', '1596900000', '0');
INSERT INTO `notifications` VALUES ('37', 'unread_followeds_posts_count', '4', '1596900000', '0');
INSERT INTO `notifications` VALUES ('38', 'unread_comments_likes_count', '4', '1596900000', '0');
INSERT INTO `notifications` VALUES ('39', 'unread_posts_likes_count', '4', '1596900000', '0');
INSERT INTO `notifications` VALUES ('50', 'unread_posts_likes_count', '7', '1596980000', '0');
INSERT INTO `notifications` VALUES ('51', 'unread_follows_count', '7', '1596980000', '0');
INSERT INTO `notifications` VALUES ('52', 'unread_comments_likes_count', '7', '1596980000', '0');
INSERT INTO `notifications` VALUES ('53', 'unread_recived_comments_count', '7', '1596980000', '0');
INSERT INTO `notifications` VALUES ('58', 'unread_messages_count', '2', '1596990000', '0');
INSERT INTO `notifications` VALUES ('67', 'unread_comments_likes_count', '2', '1597060000', '3');
INSERT INTO `notifications` VALUES ('72', 'unread_follows_count', '4', '1597060000', '0');
INSERT INTO `notifications` VALUES ('75', 'unread_posts_likes_count', '2', '1597060000', '2');
INSERT INTO `notifications` VALUES ('83', 'unread_followeds_posts_count', '8', '1597070000', '0');
INSERT INTO `notifications` VALUES ('85', 'unread_recived_comments_count', '4', '1597070000', '0');
INSERT INTO `notifications` VALUES ('91', 'unread_follows_count', '8', '1597130000', '0');
INSERT INTO `notifications` VALUES ('95', 'unread_recived_comments_count', '10', '1597150000', '0');
INSERT INTO `notifications` VALUES ('96', 'unread_posts_likes_count', '10', '1597150000', '0');
INSERT INTO `notifications` VALUES ('101', 'unread_comments_likes_count', '10', '1597150000', '0');
INSERT INTO `notifications` VALUES ('104', 'unread_recived_comments_count', '8', '1597150000', '0');
INSERT INTO `notifications` VALUES ('105', 'unread_messages_count', '8', '1597150000', '0');
INSERT INTO `notifications` VALUES ('106', 'unread_recived_comments_count', '2', '1597150000', '1');
INSERT INTO `notifications` VALUES ('110', 'unread_posts_likes_count', '8', '1597150000', '1');
INSERT INTO `notifications` VALUES ('112', 'unread_comments_likes_count', '8', '1597150000', '1');

-- ----------------------------
-- Table structure for `posts`
-- ----------------------------
DROP TABLE IF EXISTS `posts`;
CREATE TABLE `posts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `summary` text,
  `body` text,
  `timestamp` datetime DEFAULT NULL,
  `views` int(11) DEFAULT 0,
  `author_id` int(11) DEFAULT 1,
  PRIMARY KEY (`id`),
  KEY `author_id` (`author_id`),
  KEY `ix_posts_timestamp` (`timestamp`),
  CONSTRAINT `posts_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of posts
-- ----------------------------
INSERT INTO `posts` VALUES ('5', '风口浪尖的碧桂园到底做错了什么？', '国家调控着，更有未来还会有房地产税，各大房企这两年面对的压力越来越大。一部分中小房企在这一波国家调控中湮没在历史长河中，而各大扛鼎房企也不断在转型和改变自己。去年末今年初，融创通过收购万达部分产业来进行资金转换，一时间各大媒体头条都是融创的新闻，各大房地产资深新媒体各种分析稿件错层迭出，风头无两。', '# 最近，又一个扛鼎房企占据了各大媒体头条，但并不是以融创正面形式，而是各种负面新闻出现，这个房企的名字叫——碧桂园。\r\n\r\n说来也奇怪，不只是命运的差使还是自己作死，很多龙头房企在某一年变得很艰难。万科和恒大都在2008年迎来了企业低谷，而2018年则注定成为了碧桂园噩梦连连的一年。\r\n\r\n2018年上半年，一本《我在碧桂园的1000天》引起了社会大众特别是房地产业界对于碧桂园公司文化的吐槽，到了下半年刚开始，工地坍塌、人员伤亡……隔三差五的这些负面消息占据了各大媒体网站和自媒体的头条。\r\n\r\n关乎人命、关乎安居乐业，这已经不再是房地产行业内部的事情，而是全社会的事情。碧桂园的品牌和公关团队估计在这个时候忙的焦头烂额还没有个好结果。\r\n\r\n# 碧桂园到底做错了什么？为什么生活和现实在2018年终于对碧桂园动刀了呢？我们一起来看一下。\r\n\r\n把碧桂园直接推到风口浪尖的是——2018年7月26日晚，碧桂园在安徽六安的项目建筑工地发生了坍塌事故，直接导致了6人死亡。\r\n\r\n虽然事后，碧桂园发布了声明，便是该项目停工检查，排除一切潜在的不安全因素。但是最近碧桂园所发生的事情还是被民众挖了出来——2018年6月24日，碧桂园上海奉贤项目售楼处坍塌，导致1人死亡9人受伤；2018年7月12日，碧桂园杭州萧山项目地基出现裂痕，工地附近路面出现小段塌方，导致项目附近的一栋三层楼房直接变成了危房。\r\n\r\n# 到底是什么导致了碧桂园如此的局面呢？不断有事故发生到底是什么原因呢？\r\n\r\n回到5年前，或许不是很多购房者都知道碧桂园，虽然碧桂园一直处于行业的上流，但是它太低调了，公司的战略部署一般都是在三四线城市。但是2016年，碧桂园突然发力，然后在2017年的时候出人意料的成为了中国第一大房企，大到了业界人士谈房企排行的时候只考虑第二名是谁的地步。\r\n\r\n\r\n\r\n2016年实现了3000亿、2017年5508亿、2018年截止至8月1日4600亿，碧桂园不断用完美的成交数字来告诉业界，我就是行业老大！但是殊不知，在这些数字的背后都是些什么。碧桂园老总杨国强对外一直宣称：碧桂园的房子是全中国性价比最高的，又好又便宜。说实话，小编以从事房地产行业6年的职业生涯发誓，碧桂园的房子便宜是真，但是质量嘛，呵呵，估计是全中国造价最便宜的了。\r\n\r\n这段时间的各种事故就已经说明了，在风光无两的成交数据背后，是房子的质量问题，是房子材料的以次充好，是建筑过程中的偷工减料。行业里有个关于碧桂园的小故事：碧桂园在面对一个项目的一个柱体结构的时候，负责人问这是干嘛用的，设计回答：抗震用的，当地的设计要求必须抗震5级，后来老大问到：这个城市有发生过地震么？后来查下来，有史以来5级以上地震只发生了一次，而且是在隋朝。后来，最终会议决定，用于防震的柱子，取消了……取消了！这是多么奇特的脑回路！碧桂园竟然在最基本的民生保障上开玩笑。\r\n\r\n另外，一个公司的作为和高层领导的决策息息相关。那么我们就要在这里说说，上文中提到的，碧桂园的老总杨国强。不了解房地产行业的人会被外界的论调所迷惑：杨国强是一个底层出来的人，读书不多，老实本分，不做违法的事情。但是《我在碧桂园的1000天》里披露出来的杨国强却不是这个模样，而是强势而又敢打破常规，是一个十足的“疯子”。\r\n\r\n为什么说他是敢于打破常规的“疯子”，最主要的是体现在碧桂园一直强调的“高周转”上。碧桂园为了做到“高周转”，将业界的标准——拿地之后4个月开盘、5个月资金回正、6个月资金再周转的“456”变成了“345”。\r\n\r\n\r\n\r\n而通过这个模式来达到“高周转”的，碧桂园不是第一家。万科在10多年前曾经以“拿地后5个月动工、9个月销售、第一个月售出8成、产品必须6成为住宅”的“5986”来做到万科的“高周转”。但是2010年后，万科放弃了这个模式，理由则是如今碧桂园所面临的——施工安全、工程质量、社区品质、财务安全等一系列的问题。万科放弃的事情，碧桂园要不断强调，还要做出高水平，是解决了上述安全问题了吗？事实已经给出了答案，也说明了如今碧桂园所面临的问题真的是自己作死，怪不得别人。\r\n\r\n如今全国楼市都很注重安全问题，而其他扛鼎房企都把所建住宅的安全问题放在首位，这是对购房者的负责任，也是对自己品牌口碑的维护。真的不太理解，作为一个扛鼎房企，会犯下这种错误。当然我们在这里也期待碧桂园能够通过之前发生的事故来反省自己，彻底排查整顿潜在的安全隐患，做出检讨和修正，在追求“高周转”的同时能确保房屋质量，对购房者负责，对社会负责。', '2020-08-07 15:13:26', '17', '2');
INSERT INTO `posts` VALUES ('6', '中央出台棚改货币化收紧措施 房价是否会受到影响呢？', '前天央行定向降准7000亿，房地产行业内充满了一片叫好声，都在说这一举措将把严控下的楼市带出泥沼。但是很多人却发现，大部分的房企股票一路下跌，究其原因，就在于前日市场上出现了这样一则消息——棚改即将取消货币化安置政策。', '![输入图片说明](http://static.fangjia.com/stc/fs/CD03C506F32BDF378B419074CA2A21657FB6E45B37D83AED961F86A7CC0E6846F4C1715B81DA9AC67177499A67FCCAF2333DCD14B1D3BC88DB9068A666CBCCDB \"在这里输入图片标题\")\r\n### 对此，国开行发出回应：“并未暂停所有棚改项目，进行中的项目仍在持续执行，但早前总行收回了棚改项目的合同审批权限，早前在分支行可签订的合同，现在也必须由总行审批。”\r\n\r\n\r\n划重点，取消货币化安置是假的，但是上移资金审核权限却是板上钉钉的大事，这从侧面可以反映了目前全国棚改资金正在收紧。那么这到底是怎么发生的呢？而这对于房地产市场会有什么样的影响呢？\r\n\r\n![输入图片说明](http://static.fangjia.com/stc/fs/CD03C506F32BDF378B419074CA2A216513551F689B3B36D756A19565E92785480AEBA7D65197CF1C7177499A67FCCAF2333DCD14B1D3BC88DB9068A666CBCCDB \"在这里输入图片标题\")\r\n\r\n# 一、为什么会有这么大的反响？\r\n\r\n\r\n说到这个，我们首先要把以下几个名词了解清楚：\r\n\r\n\r\n棚改——是指城市对于区域范围内、平房密度大、使用年限久、房屋质量差、人均建筑面积小、基础设施配套不齐全、交通不便利、治安和消防隐患大、环境卫生脏、乱、差的区域及“城中村”拆迁再建。\r\n\r\n\r\n货币化安置（拆迁费）——棚改在初期是以实物安置的模式为主，后来由于效率比较低，所以政府采用了货币安置，即当你家房子拆迁了，政府会按照人头或者房屋面积用资金的方式（拆迁费）来补贴你家，以解决后期全家居住生活问题。\r\n\r\n![输入图片说明](http://static.fangjia.com/stc/fs/CD03C506F32BDF373FB39A4572469DD630C51D8987FC5FD7E077B5E2EE900FCFA5DC4CDBBADAEC83E1395E9D25D256FE529B0C3FE0309DD2A6E50D9F1F515F04 \"在这里输入图片标题\")\r\n\r\n至于这笔补贴费用怎么来，那么我们就要了解另一个专业名词——PSL。\r\n\r\n\r\n\r\nPSL——抵押补充贷款（PSL，即Pledged Supplementary Lending的缩写），PSL作为一种新的储备政策工具，有两层含义，首先量的层面，是基础货币投放的新渠道；其次价的层面，通过商业银行抵押资产从央行获得融资的利率，引导中期利率。\r\n\r\n那么为什么叫停棚改资金会有这么大的一个反响呢？\r\n\r\n\r\n2015-2017年这三年间，全中国一共改造了大概约1450万套棚户区住房。货币化安置的比例也逐渐从30%一路提高到了50%，甚至一些三四线城市达到了80%。\r\n\r\n\r\n换个更加直观的说法， 2017年，全中国一手房成交面积约169408万平方米，按照一套100平方米计算的话，就是大约1694万套一手房完成成交。而之前每年平均500万套的棚户区住房，也就是占了一手房年成交的三分之一，这相当于一些中型房企1年乃至3年的成交量。\r\n\r\n全部\r\n行业动态\r\n数据分析\r\n成功案例\r\n公司动态\r\n中央出台棚改货币化收紧措施 房价是否会受到影响呢？\r\n\r\n浏览：5315分享到：    \r\n前天央行定向降准7000亿，房地产行业内充满了一片叫好声，都在说这一举措将把严控下的楼市带出泥沼。但是很多人却发现，大部分的房企股票一路下跌，究其原因，就在于前日市场上出现了这样一则消息——棚改即将取消货币化安置政策。\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n对此，国开行发出回应：“并未暂停所有棚改项目，进行中的项目仍在持续执行，但早前总行收回了棚改项目的合同审批权限，早前在分支行可签订的合同，现在也必须由总行审批。”\r\n\r\n\r\n划重点，取消货币化安置是假的，但是上移资金审核权限却是板上钉钉的大事，这从侧面可以反映了目前全国棚改资金正在收紧。那么这到底是怎么发生的呢？而这对于房地产市场会有什么样的影响呢？\r\n\r\n\r\n\r\n\r\n一、为什么会有这么大的反响？\r\n\r\n\r\n说到这个，我们首先要把以下几个名词了解清楚：\r\n\r\n\r\n棚改——是指城市对于区域范围内、平房密度大、使用年限久、房屋质量差、人均建筑面积小、基础设施配套不齐全、交通不便利、治安和消防隐患大、环境卫生脏、乱、差的区域及“城中村”拆迁再建。\r\n\r\n\r\n货币化安置（拆迁费）——棚改在初期是以实物安置的模式为主，后来由于效率比较低，所以政府采用了货币安置，即当你家房子拆迁了，政府会按照人头或者房屋面积用资金的方式（拆迁费）来补贴你家，以解决后期全家居住生活问题。\r\n\r\n\r\n\r\n\r\n\r\n至于这笔补贴费用怎么来，那么我们就要了解另一个专业名词——PSL。\r\n\r\n\r\n\r\nPSL——抵押补充贷款（PSL，即Pledged Supplementary Lending的缩写），PSL作为一种新的储备政策工具，有两层含义，首先量的层面，是基础货币投放的新渠道；其次价的层面，通过商业银行抵押资产从央行获得融资的利率，引导中期利率。\r\n\r\n\r\n\r\n那么为什么叫停棚改资金会有这么大的一个反响呢？\r\n\r\n\r\n2015-2017年这三年间，全中国一共改造了大概约1450万套棚户区住房。货币化安置的比例也逐渐从30%一路提高到了50%，甚至一些三四线城市达到了80%。\r\n\r\n\r\n换个更加直观的说法， 2017年，全中国一手房成交面积约169408万平方米，按照一套100平方米计算的话，就是大约1694万套一手房完成成交。而之前每年平均500万套的棚户区住房，也就是占了一手房年成交的三分之一，这相当于一些中型房企1年乃至3年的成交量。\r\n\r\n\r\n\r\n而且棚改造成的“增量”是刚需“增量”，不仅能满足目前市场上的主流客户——刚需置业的房源需求，还能拉动投资做到去库存，也是改善城市面貌的必须要做的事情，这也是为什么多地政府热衷棚改的主要原因。\r\n\r\n\r\n# 二、为什么现在棚改货币化要收紧？\r\n\r\n\r\n棚改的主动权其实是一直不在地方政府，而是在中央政府，而已经发放的棚改资金在2014年大量发放后，如果中央不对其进行结构性的调整，那么国家后期将面临着还本付息带来的一大笔资金，会对国家财政造成比较大的压力。\r\n\r\n\r\n这里有一组psl的发放总量和贷款中的占比数据：\r\n![输入图片说明](http://static.fangjia.com/stc/fs/CD03C506F32BDF37809BC2BD134F96EDBAFB55D34D4788BB6FC25EF3E7B04E6A2B4794FBFABC120724104B742B8971FB03EE789FBA7C3F37 \"在这里输入图片标题\")\r\n\r\n# 三、货币化收紧对于房企和房价的影响？\r\n\r\n\r\n（1）对房企的影响——此次国开行的合同审批权上移，并不意味着棚改的资金会大量减少，今后将更多的通过棚改专项债的方式向市场注入资金。由于紧预期的基调不变，开发商对于这种情况已经有了预料，对于在全国都有布局的房企来说不会有影响，而对于那些在特定城市布局的房企来说会有一定程度的影响。\r\n\r\n\r\n（2）对房价的影响——棚改对于一二线城市房价基本没什么影响，因为在一二线城市棚改并不是楼市主流业务，而对于三四线城市房价的影响是通过影响房企来间接实现的。对已经审批的项目没什么影响，但是货币化收紧对后期的影响是存在的，不会导致三四线城市价格暴涨，但是稳步上涨的压力还是存在的。', '2020-08-07 15:22:48', '14', '3');
INSERT INTO `posts` VALUES ('7', '上海13号线西延伸段已确定 华漕板块迎来利好曙光', '熟悉13号线的小伙们的肯定知道，当年世博会期间，13号线前期（马当路站—世博大道站）作为世博专用线，线路走向比较好，实现了上海N多条地铁换乘，确保了当时观博客流的交通输送。', '## 计划于今年通车的13号线二期、三期主要走向向东延伸，途径浦东三林、北蔡以及张江区域，其中二期为8座车站，三期为3座车站，东延段都集中于浦东区域。\r\n\r\n\r\n根据《上海市轨道交通近期建设规划(2017-2025)环境影响评价第二次公示》的公示文件，13号线还将详细延伸至大虹桥区域，站点目前已确定为六站，分别是中国博览会北站，运乐路站，闵北路站，纪展路站，纪翟路站和开兴路站。除了终点站，其余五站都位于闵行区域的华漕板块，这样将是该区域首次接入的轨交线路。预估该条线路将于2020年通车，到那时，肯定也会带动站点房地产市场的发展和周边配套的成熟。\r\n\r\n\r\n而现阶段13号线西延段房地产市场又是如何呢？我们一起往下看：\r\n# 中国博览会北站\r\n中国博览会北站位于诸光路、崧泽高架路口南侧，沿诸光路南北向布置。该站主要服务于国家会展中心。\r\n![输入图片说明](http://static.fangjia.com/stc/fs/CD03C506F32BDF37226027B82EA3E8368E2B7D52DC4F946B3C054CC935F0EB6D33CF2E5831CC8173919F1CFB005B17D0AD680C3EF462CB81 \"在这里输入图片标题\")\r\n\r\n从地图上来看，站点附近位于青浦徐泾和闵行华漕板块搭界处，周边主要虹桥世界中心，西郊花园、西郊庄园、玉兰清苑、二联馨苑、紫薇新村、香港花园等住宅，目前均为二手房，由于青浦徐泾板块周边的二手房离国家会展中心等其他大虹桥商业中心距离更近，此外还有17号线（即将通车）和2号线的轨交影响，该板块的二手房目前挂牌价在5.4万/平左右，该站点附近的住宅，整体挂牌均价在6万/平左右，例如：西郊大公馆目前挂牌价在5.7万/平，久事西郊花园6.6万/平，新虹桥雅苑5.9万/平。而闵行华漕板块的价格，挂牌价大概在6.1万/平，距离该站点附近较近的二手房挂牌在4万/平，例如紫薇新村挂牌价在4.3万/平，香港花园价格在4.4万/平。\r\n\r\n# 运乐路站\r\n运乐路站位于金丰路、运乐路路口东南象限地块内，沿金丰路南北向布置。\r\n![输入图片说明](http://static.fangjia.com/stc/fs/CD03C506F32BDF37C98873D710995FD17C52E26C3501913277D828AB746A563132412ED079B8AF37919F1CFB005B17D0AD680C3EF462CB81 \"在这里输入图片标题\")\r\n目前站点附近有新房西郊庄园马德里洋房、金球怡云花园玫瑰里。目前西郊庄园马德里洋房目前在售房源均价7万/平，主要有大平层户型建面220-300平（所剩房源不多，楼层可选择性小），复式户型建面380平-470平。金球怡云花园玫瑰里目前剩余少量联排别墅在售，房源均价65000元/平，主要户型为建面230平和248平联排别墅。目前站点附近的二手房价大概在4.5万/平左右，如金丰小区价格大概在4.3万/平，美邻苑价格大概在4.7万/平，西庭网球俱乐部和公寓均价4.9万/平。不过瑞生花园相比较高，挂牌均价大概在6.4万/平。\r\n# 闵北路站\r\n![输入图片说明](http://static.fangjia.com/stc/fs/CD03C506F32BDF37C98873D710995FD1AF3C477693D0D1657ECF7FD5AB690EB2F6368F9982C6305E919F1CFB005B17D0AD680C3EF462CB81 \"在这里输入图片标题\")\r\n站点西侧为规划上海新虹桥国际医学中心，东侧为融信绿地国际商业广场，北侧为上海韩国学校、台商子女学校和上海新加坡国际学校，南侧为林茵湖畔园商品房住宅小区。\r\n\r\n\r\n周边二手房挂牌价大概在6万/平左右，例如：林茵湖畔公寓挂牌价在5.8万/平，别墅挂牌价在6.1万/平，万科红郡6.8万/平。虽然商业中心、医院、学校一应俱全，但是整体区域还是处于城市开发不太成熟的阶段，在未来还有更多的可塑性和发展空间，所以对于附近区域的购房者来说，这区域的二手房还算是挺不错的选择。\r\n\r\n# 开兴路站\r\n开兴路站位于开兴路、纪嵩路路口东侧地块内，自开兴路、纪嵩路路口呈东西向布置。\r\n![输入图片说明](http://static.fangjia.com/stc/fs/CD03C506F32BDF378EF707D073729C31B1AA827F2E6AD1EFB2793D1B30B49942D4E39C971122069E919F1CFB005B17D0AD680C3EF462CB81 \"在这里输入图片标题\")\r\n站点北侧为农田，南侧为民房（图上是称为“西八图”的村宅，开兴路应为南北向规划图），属于还未开发的区域，所以没有什么房源可以进行推荐。\r\n\r\n\r\n总的来说，13号线西延伸段沿线还是以工业区和民房为主，在居住环境等方面来看的话，闵北路站、运乐路站和中国博览会北站比较适宜，无论是配套设施还是开发成熟度都已经还算可以，另外纪翟路站沿线虽然近距离的小区比较少，但是用共享单车骑上个10分钟左右，那房源的选择性还是相当多的。而且13号线西延伸段沿线以刚需为主，改善为辅，在选择时还是需要根据自身来考虑。', '2020-08-08 07:32:00', '25', '2');
INSERT INTO `posts` VALUES ('8', '张爱玲笔下的避世之地 上海逝去的城市回忆', '寻常巷陌里小贩的叫卖声，孩子的喧闹，妇女们的闲言碎语，厨房里飘着的油烟味……当听到弄堂一词时，或许这些词会脱口而出，因为它是上海最真实的一部分，是人们日常生活的体现。', '和弄堂一样，洋房也是上海开埠后的产物，但它却是上海最精致的一部分；这也许是我们听过的最恰当的比喻，如果把上海比作一件华丽的旗袍，那么洋房一定是这件旗袍上最精致的盘相扣。\r\n![输入图片说明](http://static.fangjia.com/stc/fs/CD03C506F32BDF37450322D9A1683CCEC09113F42802DB7A275737630F8305125E380C5D57D17B9C7177499A67FCCAF2333DCD14B1D3BC88DB9068A666CBCCDB \"在这里输入图片标题\")\r\n\r\n### 道不尽的洋房故事\r\n\r\n\r\n\r\n在那么多写上海的文章中，洋房作为重要场景多次出现在张爱玲的作品中。无论是《倾城之恋》中白流苏逃离的白公馆，还是《沉香屑》中葛薇龙姑母的奢华豪宅，张爱玲都用了大量笔墨写作了他们居住的洋房，以至于现在仍有大量读者在寻找着她笔下的洋房究竟在哪儿。\r\n\r\n\r\n\r\n《倾城之恋》中的白公馆戒备森严，房子与房子间隔着宽阔地，《色戒》中的老洋房有着红瓦陡屋顶和哥特式壁炉烟囱，《沉香屑》中的豪宅有着依稀可见的黄地红边的窗棂……\r\n\r\n\r\n而出现在张爱玲《洋房生活记趣》一文中的洋房则是一栋被刷成黛粉色的七层西式公寓，也就是现在常德路路口的爱丁堡公寓。这是繁华市中心的一处宁静居所，有着花园洋房独特的气质。\r\n\r\n\r\n“洋房是最合理想的逃世的地方。厌倦了大都会的人们，往往记挂着和平幽静的乡村，心心念念盼望着有一天能够告老归田，养蜂种菜，享点清福，殊不知在乡下多买半斤腊肉便要引起许多闲言闲语，而在洋房的最上层你就是站在窗前换衣服也不妨事。”大隐隐于市大抵就是如此吧。\r\n![输入图片说明](http://static.fangjia.com/stc/fs/CD03C506F32BDF375B258DB31D611E07EC12D2CC866CB01A8669ED1872C15E59B8A28F65F31DA7647177499A67FCCAF2333DCD14B1D3BC88DB9068A666CBCCDB \"在这里输入图片标题\")\r\n\r\n### 洋房——上海开埠后的产物\r\n\r\n\r\n\r\n1843年，上海正式开埠。也正是在那个时候，上海洋房的历史由此拉开了序幕。据资料记载，这一时期的洋房讲究排场，平面布局铺张，内部装饰极尽奢华，仿早期欧式建筑风格，殖民统治者、清廷命官以及商业巨头视洋房为他们生活的乐土。传说中李鸿章金屋藏娇的丁香花园就是这一时期的代表作，西式房屋的格局，配以中式庭院的小桥流水，曲径通幽，别具一格。\r\n\r\n随着西方势力的不断加强，西方的金融界人士、军政要人移居至此。同时，待到18世纪中后期，租界的现代化效应的显现，上海逐渐成为冒险的乐园，出现了江浙沪一带的富商、纨绔子弟涌入上海租界的趋向。在《海关十年报告》中，就记载了上述的现象，“这里房租之贵和捐税之重超过中国的多数城市。但是由于人身的财产更为安全，生活较为舒适，有较多的娱乐设施，又处于交通运输的中心位置，许多退休和待职的官员现在在这里住家，还有许多富商也在这里。”谁不想在这繁华地带有一处自己的独立住宅呢？租界内的洋房也日益受到中国人的重视。\r\n![输入图片说明](http://static.fangjia.com/stc/fs/CD03C506F32BDF375B258DB31D611E07C70C01D1356CF22C7F7FC807E08C36B9099DE52535CC8D2A7177499A67FCCAF2333DCD14B1D3BC88DB9068A666CBCCDB \"在这里输入图片标题\")\r\n\r\n### 20世纪20年代-40年代的洋房繁盛期\r\n\r\n\r\n20世纪20年代，租界开始扩张，沿着南京路和淮海中路干道由东向西分布，法租界与华界的界限日益清晰。从那时起，这里就被认为上海最好的地段，各路权贵们都开始买地建房。在1920年的《海关十年报告》中，就有这样一句话，“1920年前的八年里，法租界共有欧洲人住宅432幢，而1920年和1921年两年里就造了552幢”。根据法租界的规定，这些住宅或是“连幢房屋”，或是“单宅或双宅房屋”，且配置了暖气设备（或壁炉）和卫生设备，有的还带有游泳池、子弹房和球场。\r\n\r\n\r\n上海开埠后，带来的不仅是殖民时代的开始，还有西方的文化、建筑和贸易。这一时期，邬达克等著名的设计师来到上海，建造了一批风格迥异的西式洋房。英国乡村风格的洋房、西班牙风格、混合式风格、意大利巴洛克风格等多元化建筑风格的洋房不断涌现。它们位于“上只角”，周围是上海顶级商业区；它们出自国外顶级设计师之手，掩映在成群的法国梧桐中。而它们多样化的建筑风格仍被沿用至今。\r\n\r\n\r\n这一带成为了中外达官显贵和商人巨贾的聚集地，甚至每一栋都承载着1至2个上海滩的传奇故事，是真正意义上的“富人的天堂”。\r\n\r\n\r\n1937年，中国正处于紧张局面中，少有巨资兴建别墅。1945年抗日战争胜利后，上海通货膨胀严重，一些资本家开始兴建别墅，作为不动产投资。这一时期的洋房趋于现代化，外形多采用国际流行样式，花园洋房渐渐走向了尾声。\r\n\r\n\r\n“旧时王谢堂前燕”，1949年解放后，洋房收归国有，逐渐淡出了人们的视野。\r\n![输入图片说明](http://static.fangjia.com/stc/fs/CD03C506F32BDF371B9AB037BA09A388545647332039A167D4ED4D0C2FF7085FE7848A90FB3B9C197177499A67FCCAF2333DCD14B1D3BC88DB9068A666CBCCDB \"在这里输入图片标题\")\r\n\r\n### 购买一栋花园洋房需要多少钱？\r\n\r\n\r\n1998年，老洋房开始上市，允许私人买卖。由于其稀缺性和文化价值，这些独门独户带花园的洋房日益成为市场的宠儿，或被用作办公地点，或被用来作为酒店，抑或被境外人士、华裔所购买用于收藏。现在黄浦、徐汇、静安等曾经的租界地带仍保留了大量独门独户带花园的洋房。而这些洋房中，产权清晰的不过百来栋。\r\n\r\n\r\n\r\n物以稀为贵，花园洋房每平米的售价远高于黄浦江一带的豪宅。2003年前后，老洋房的价格为每平米1万至3万元，一套建筑面积700平，花园500平的房子，总价为2500-3000万元。而十年后，一栋花园洋房的售价翻了几倍。\r\n\r\n2017年11月初，绍兴路54号的杜月笙公馆以6亿进行出售，这栋洋房共6幢楼，占地4321平，花园面积2600平，每平米的均价约12万，且附赠了大量的附带面积。\r\n\r\n\r\n这些上海老洋房承载了上海的繁华与传奇，早已成为了上海滩的符号。漫步在满是梧桐的街道上，那一栋栋老洋房被梧桐树所包围，墙面的红磁瓦，斜坡陡屋顶，屋内氤氲着的浅黄色灯光，飘出的阵阵琴声，总能引人无限遐想。', '2020-08-10 12:03:16', '32', '8');
INSERT INTO `posts` VALUES ('9', 'test', '熟悉13号线的小伙们的肯定知道，当年世博会期间，13号线前期（马当路站—世博大道站）作为世博专用线，线路走向比较好，实现了上海N多条地铁换乘，确保了当时观博客流的交通输送。', 'test', '2020-08-11 12:05:42', '11', '8');

-- ----------------------------
-- Table structure for `posts_likes`
-- ----------------------------
DROP TABLE IF EXISTS `posts_likes`;
CREATE TABLE `posts_likes` (
  `user_id` int(11) DEFAULT NULL,
  `post_id` int(11) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  KEY `fk_posts_likes_post_id_posts` (`post_id`),
  KEY `fk_posts_likes_user_id_users` (`user_id`),
  CONSTRAINT `fk_posts_likes_post_id_posts` FOREIGN KEY (`post_id`) REFERENCES `posts` (`id`),
  CONSTRAINT `fk_posts_likes_user_id_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of posts_likes
-- ----------------------------
INSERT INTO `posts_likes` VALUES ('7', '5', '2020-08-09 14:53:07');
INSERT INTO `posts_likes` VALUES ('7', '7', '2020-08-10 08:24:28');
INSERT INTO `posts_likes` VALUES ('2', '8', '2020-08-10 12:06:53');
INSERT INTO `posts_likes` VALUES ('4', '5', '2020-08-10 12:58:09');
INSERT INTO `posts_likes` VALUES ('8', '5', '2020-08-11 12:03:59');
INSERT INTO `posts_likes` VALUES ('10', '5', '2020-08-11 12:17:18');
INSERT INTO `posts_likes` VALUES ('10', '8', '2020-08-11 12:17:59');
INSERT INTO `posts_likes` VALUES ('8', '8', '2020-08-11 12:19:33');
INSERT INTO `posts_likes` VALUES ('8', '7', '2020-08-11 12:20:46');
INSERT INTO `posts_likes` VALUES ('8', '9', '2020-08-11 13:12:59');

-- ----------------------------
-- Table structure for `roles`
-- ----------------------------
DROP TABLE IF EXISTS `roles`;
CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `slug` varchar(64) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `default` tinyint(1) DEFAULT NULL,
  `permissions` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_roles_slug` (`slug`),
  KEY `ix_roles_default` (`default`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of roles
-- ----------------------------
INSERT INTO `roles` VALUES ('1', 'shutup', '小黑屋', '0', '0');
INSERT INTO `roles` VALUES ('2', 'reader', '读者', '1', '3');
INSERT INTO `roles` VALUES ('3', 'author', '作者', '0', '7');
INSERT INTO `roles` VALUES ('4', 'administrator', '管理员', '0', '135');

-- ----------------------------
-- Table structure for `users`
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(64) DEFAULT NULL,
  `email` varchar(120) DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  `name` varchar(64) DEFAULT NULL,
  `location` varchar(64) DEFAULT NULL,
  `about_me` text,
  `member_since` datetime DEFAULT NULL,
  `last_seen` datetime DEFAULT NULL,
  `last_followeds_posts_read_time` datetime DEFAULT NULL,
  `last_follows_read_time` datetime DEFAULT NULL,
  `last_recived_comments_read_time` datetime DEFAULT NULL,
  `last_messages_read_time` datetime DEFAULT NULL,
  `last_comments_likes_read_time` datetime DEFAULT NULL,
  `last_posts_likes_read_time` datetime DEFAULT NULL,
  `confirmed` tinyint(1) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_users_username` (`username`),
  UNIQUE KEY `ix_users_email` (`email`),
  KEY `fk_users_role_id_roles` (`role_id`),
  CONSTRAINT `fk_users_role_id_roles` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('1', 'superadmin', 'superadmin@superadmin.com', 'pbkdf2:sha256:150000$Kx9O0VNW$fca54e29dfb528905bc2296921b7ce25c67b4bbdb942464de65e16c75b508969', '房价资讯机器人\r\n', null, null, '2020-08-11 15:25:24', '2020-08-11 15:28:52', null, null, null, null, null, null, '1', '4');
INSERT INTO `users` VALUES ('2', 'wangliang', 'shiqinze7@163.com', 'pbkdf2:sha256:150000$bm2Yv2fc$1249148a958cc7ed77c246b7d4b17ec41b1e74482f5f0518ab167bcf493f9683', '王亮', 'whu', 'madman', '2020-08-07 15:10:32', '2020-08-11 07:01:02', null, '2020-08-08 14:31:20', '2020-08-09 15:29:23', '2020-08-09 14:53:25', null, '2020-08-09 15:29:29', '1', '3');
INSERT INTO `users` VALUES ('3', 'zhanglei', 'xuanlvyin79@163.com', 'pbkdf2:sha256:150000$fcqwt1gN$baa3e43b64d367b2133515558e18e28bce77aaa30b77e6628a43ba4b8ba607b9', '张雷', 'whu', 'man with logic', '2020-08-07 15:18:57', '2020-08-10 01:50:47', null, null, '2020-08-08 08:29:39', null, null, null, '1', '3');
INSERT INTO `users` VALUES ('4', 'test', 'test@test.com', 'pbkdf2:sha256:150000$WZczh21U$d7759c702b02e8eafc9c0b01d6cfea8ddf569f2950e351fea2a9a9d88c63845b', '测试初号机', 'unknown', 'test man', '2020-08-08 14:27:57', '2020-08-11 13:03:35', '2020-08-08 14:56:10', '2020-08-10 12:13:16', '2020-08-10 14:30:36', '2020-08-08 14:32:07', '2020-08-08 14:56:11', '2020-08-08 14:56:14', '1', '2');
INSERT INTO `users` VALUES ('5', 'wangzhihao', '13451142805@163.com', 'pbkdf2:sha256:150000$gVSpkEB0$3572780d03aacaa44cbcb733ccc0ad3735f7cac9d6430f1c76b71fd6188c59d7', null, null, null, '2020-08-09 12:38:22', '2020-08-09 16:51:01', null, null, null, null, null, null, '1', '2');
INSERT INTO `users` VALUES ('6', 'mangwugo', 'm17133369035@163.com', 'pbkdf2:sha256:150000$ptIqL3ez$8ef5459cc0616cd513aa78fee9fd21713fa8d0cbf87ac3a02a9f28b1a1545282', null, null, null, '2020-08-09 13:18:10', '2020-08-09 13:27:32', null, null, null, null, null, null, '1', '2');
INSERT INTO `users` VALUES ('7', 'mangwugogo', '3273250738@qq.com', 'pbkdf2:sha256:150000$BjS8Csxf$a54a9a5204c671e25a3a23085c83ab324339d7029d8473f5bf16b81f8657b4ea', null, null, null, '2020-08-09 14:49:54', '2020-08-10 08:24:39', null, '2020-08-09 14:52:21', '2020-08-09 14:52:58', null, '2020-08-09 14:52:22', '2020-08-09 14:52:21', '1', '3');
INSERT INTO `users` VALUES ('8', 'mangwu', '1185956753@qq.com', 'pbkdf2:sha256:150000$BH3x6BkF$a5c48a70b8c674c51807277b8f7575d9a0d0f889645888586ab8d39d31c1c9ad', '汪志豪', 'whu', '123', '2020-08-09 16:27:08', '2020-08-11 13:45:00', '2020-08-10 13:47:18', '2020-08-11 07:55:39', '2020-08-11 12:21:35', '2020-08-11 12:07:08', '2020-08-11 07:55:38', '2020-08-11 07:55:39', '1', '4');
INSERT INTO `users` VALUES ('9', 'test2', 'test2@test.com', 'pbkdf2:sha256:150000$LCDV2lXO$31cdf6292a21ab3df2011618a98c9a4720ce24a28c7b65866ec9ff741787cff3', null, null, null, '2020-08-10 12:10:02', '2020-08-10 13:47:35', null, null, null, null, null, null, '1', '2');
INSERT INTO `users` VALUES ('10', 'test3', 'test3@test.com', 'pbkdf2:sha256:150000$XXmsUVaU$e0febcb2cfac7d53f98d238692b4b46ee1982494115002b1cecbbddb0fbc04bb', null, null, null, '2020-08-11 12:03:00', '2020-08-11 12:18:36', null, null, '2020-08-11 12:07:23', null, null, '2020-08-11 12:07:26', '1', '2');
