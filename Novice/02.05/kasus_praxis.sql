-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 17 Des 2019 pada 17.49
-- Versi server: 10.4.6-MariaDB
-- Versi PHP: 7.3.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kasus_praxis`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `salutatin`
--

CREATE TABLE `salutatin` (
  `id` int(13) NOT NULL,
  `Salutatin` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `salutatin`
--

INSERT INTO `salutatin` (`id`, `Salutatin`) VALUES
(1, 'Mr. '),
(2, 'Ms. '),
(3, 'Mrs. '),
(4, 'Dr. ');

-- --------------------------------------------------------

--
-- Struktur dari tabel `tabel1`
--

CREATE TABLE `tabel1` (
  `Membership_id` int(13) NOT NULL,
  `Full_Names` varchar(40) NOT NULL,
  `Adress` varchar(40) NOT NULL,
  `salutation_id` int(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `tabel1`
--

INSERT INTO `tabel1` (`Membership_id`, `Full_Names`, `Adress`, `salutation_id`) VALUES
(1, 'Janet Jones', 'First Street PLot No4', 2),
(2, 'Robert Phil', '3rd Street34', 1),
(3, 'Robert Phil', '5th Avenue', 1);

-- --------------------------------------------------------

--
-- Struktur dari tabel `tabel2`
--

CREATE TABLE `tabel2` (
  `membership_id` int(13) NOT NULL,
  `movie_rented` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `tabel2`
--

INSERT INTO `tabel2` (`membership_id`, `movie_rented`) VALUES
(1, 'Pirates of the Caribbean'),
(1, 'Clash of the Titans'),
(2, 'Forgetting Sarah Marshal'),
(2, 'Daddys Little Girls'),
(3, 'Clash of the Titans');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `salutatin`
--
ALTER TABLE `salutatin`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `tabel1`
--
ALTER TABLE `tabel1`
  ADD PRIMARY KEY (`Membership_id`),
  ADD KEY `salutation_id` (`salutation_id`);

--
-- Indeks untuk tabel `tabel2`
--
ALTER TABLE `tabel2`
  ADD KEY `membership_id` (`membership_id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `salutatin`
--
ALTER TABLE `salutatin`
  MODIFY `id` int(13) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `tabel1`
--
ALTER TABLE `tabel1`
  ADD CONSTRAINT `tabel1_ibfk_1` FOREIGN KEY (`salutation_id`) REFERENCES `salutatin` (`id`);

--
-- Ketidakleluasaan untuk tabel `tabel2`
--
ALTER TABLE `tabel2`
  ADD CONSTRAINT `tabel2_ibfk_1` FOREIGN KEY (`membership_id`) REFERENCES `tabel1` (`Membership_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
