-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 20, 2019 at 09:36 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vash1`
--

-- --------------------------------------------------------

--
-- Table structure for table `aithouses1`
--

CREATE TABLE `aithouses1` (
  `ar_aith` int(5) NOT NULL,
  `thesh_aith` varchar(25) NOT NULL,
  `math` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `aithouses1`
--

INSERT INTO `aithouses1` (`ar_aith`, `thesh_aith`, `math`) VALUES
(4, 'plhroforikhs', 'programmatismos 1'),
(6, 'hlektrologias', 'hlektrika kyklwmata'),
(9, 'dioikish', 'mathimatika'),
(2, 'petrelaiwn', 'fysikh'),
(10, 'mathimatiko', 'algevra'),
(11, 'gymnasthrio', 'gymnastikh'),
(0, '', ''),
(13, 'diktywn', 'prwtokolla'),
(78, 'ylikou', 'sae'),
(4, 'oikonomika', 'arxes oikonomias'),
(2, 'hlektrologias', 'hlektrikes mhxanes');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
