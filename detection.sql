-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 01, 2023 at 05:28 AM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `detection`
--

-- --------------------------------------------------------

--
-- Table structure for table `junction`
--

CREATE TABLE `junction` (
  `Id` int(11) NOT NULL,
  `JName` varchar(100) NOT NULL,
  `lat` double NOT NULL,
  `lon` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `junction`
--

INSERT INTO `junction` (`Id`, `JName`, `lat`, `lon`) VALUES
(1, 'kalavasal signal1', 9.932353, 78.096445),
(2, 'kalavasal signal2', 9.931041, 78.094704),
(3, 'kalavasal signal3', 9.928821, 78.09512),
(4, 'kalavasal signal4', 9.929444, 78.096431),
(5, 'arasaradi signal1', 9.928352, 78.097793),
(6, 'arasaradi signal2', 9.929679, 78.100182),
(7, 'arasaradi signal3', 9.926029, 78.100953),
(8, 'arasaradi signal4', 9.927427, 78.10225),
(9, 'simakkal signal1', 9.924967625425344, 78.12093031049962),
(10, 'sellur signal1', 9.927961074704038, 78.12517624737671),
(11, 'sellur signal2', 9.930755, 78.12464),
(12, 'goripalayam signal1', 9.929125, 78.128315),
(13, 'goripalayam signal1', 9.929783, 78.130182);


--
-- Indexes for dumped tables
--

--
-- Indexes for table `junction`
--
ALTER TABLE `junction`
  ADD PRIMARY KEY (`Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
