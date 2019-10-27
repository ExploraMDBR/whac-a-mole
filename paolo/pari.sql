-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jul 17, 2019 at 11:28 AM
-- Server version: 10.1.19-MariaDB
-- PHP Version: 5.6.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pari`
--

-- --------------------------------------------------------

--
-- Table structure for table `autostima`
--

CREATE TABLE `autostima` (
  `genere` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `eta` varchar(2) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ruota` varchar(2) COLLATE utf8mb4_unicode_ci NOT NULL,
  `arrampicata` varchar(2) COLLATE utf8mb4_unicode_ci NOT NULL,
  `neonato` varchar(2) COLLATE utf8mb4_unicode_ci NOT NULL,
  `riflessi` varchar(2) COLLATE utf8mb4_unicode_ci NOT NULL,
  `missione` varchar(2) COLLATE utf8mb4_unicode_ci NOT NULL,
  `messaggio` varchar(2) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `autostima`
--

INSERT INTO `autostima` (`genere`, `eta`, `ruota`, `arrampicata`, `neonato`, `riflessi`, `missione`, `messaggio`) VALUES
('maschio', '6', 'si', 'si', 'si', 'si', 'si', 'si'),
('maschio', '6', 'si', 'si', 'si', 'si', 'si', 'si'),
('maschio', '6', 'si', 'si', 'no', 'no', 'no', 'si'),
('maschio', '6', 'si', 'si', 'no', 'no', 'no', 'si'),
('maschio', '6', 'si', 'si', 'no', 'no', 'no', 'si'),
('', '', '', '', '', '', '', ''),
('maschio', '6', 'si', 'si', 'no', 'no', 'no', 'si'),
('femmina', '8', 'si', 'no', 'no', 'no', 'no', 'si'),
('femmina', '8', 'si', 'no', 'no', 'no', 'no', 'si'),
('', '', '', '', '', '', '', ''),
('femmina', '8', 'si', 'no', 'no', 'no', 'no', 'si'),
('', '', '', '', '', '', '', ''),
('femmina', '8', 'si', 'no', 'no', 'no', 'no', 'si'),
('femmina', '8', 'si', 'no', 'no', 'no', 'no', 'si'),
('femmina', '8', 'si', 'no', 'no', 'no', 'no', 'si'),
('femmina', '8', 'si', 'no', 'no', 'no', 'no', 'si'),
('femmina', '8', 'si', 'no', 'no', 'no', 'no', 'si'),
('femmina', '8', 'si', 'no', 'no', 'no', 'no', 'si'),
('', '', '', '', '', '', '', ''),
('femmina', '8', 'si', 'no', 'no', 'no', 'no', 'si'),
('femmina', '6', 'si', 'no', 'no', 'no', 'no', 'si'),
('femmina', '6', 'si', 'no', 'no', 'no', 'no', 'si'),
('femmina', '6', 'si', 'no', 'no', 'no', 'no', 'si'),
('femmina', '6', 'si', 'no', 'no', 'no', 'no', 'si'),
('femmina', '6', 'si', 'no', 'no', 'no', 'no', 'si'),
('femmina', '6', 'si', 'no', 'no', 'no', 'no', 'si'),
('', '', '', '', '', '', '', ''),
('femmina', '6', 'si', 'no', 'no', 'no', 'no', 'si'),
('femmina', '6', 'si', 'no', 'no', 'no', 'no', 'si'),
('maschio', '6', 'no', 'no', 'si', 'no', 'no', 'si');

-- --------------------------------------------------------

--
-- Table structure for table `code`
--

CREATE TABLE `code` (
  `code` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `utente`
--

CREATE TABLE `utente` (
  `genere` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `eta` varchar(2) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tempo` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `note` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --
-- -- Dumping data for table `utente`
-- --

-- INSERT INTO `utente` (`genere`, `eta`, `tempo`, `note`) VALUES
-- ('', '', '0000-00-00 00:00:00', 'ok'),
-- ('', '', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', ' 6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', ' 6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', ' 6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', ' 6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', ' 6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', ' 6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', ' 6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', ' 6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', ' 6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', ' 6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', ' 6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', ' 6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', ' 6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', ' 6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', ' 6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', ' 6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', ' 6', '0000-00-00 00:00:00', 'ok'),
-- ('0126', '', '0000-00-00 00:00:00', 'ok'),
-- ('0126', '', '0000-00-00 00:00:00', 'ok'),
-- ('01', '60', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', '6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', '6', '0000-00-00 00:00:00', 'ok'),
-- ('0126', '', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', '6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', '6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', '6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', '6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', '6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', '6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', '6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', '81', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', '6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', '6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', '6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', '6', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', '12', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', '12', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', '12', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', '12', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', '12', '0000-00-00 00:00:00', 'ok'),
-- ('maschio', '12', '0000-00-00 00:00:00', 'ok');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `code`
--
ALTER TABLE `code`
  ADD PRIMARY KEY (`code`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
