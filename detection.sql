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
(1, 'kalavasal', 9.930195, 78.095655),
(2, 'Arasaradi', 9.927637, 78.099387),
(3, 'Simikkal', 9.924819, 78.121492),
(4, 'Sellur', 9.93016, 78.125973),
(5, 'Goripalayam', 9.92917, 78.128837);

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
