/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE TABLE `cliente` (
  `idcliente` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `telefone` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  PRIMARY KEY (`idcliente`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `emprestimo` (
  `idemprestimo` int NOT NULL AUTO_INCREMENT,
  `data_de_devolução` varchar(45) NOT NULL,
  `multa` varchar(45) NOT NULL,
  `cliente_idcliente` int NOT NULL,
  `livros_idlivros` int NOT NULL,
  PRIMARY KEY (`idemprestimo`),
  KEY `fk_emprestimo_cliente1_idx` (`cliente_idcliente`),
  KEY `fk_emprestimo_livros1_idx` (`livros_idlivros`),
  CONSTRAINT `fk_emprestimo_cliente1` FOREIGN KEY (`cliente_idcliente`) REFERENCES `cliente` (`idcliente`),
  CONSTRAINT `fk_emprestimo_livros1` FOREIGN KEY (`livros_idlivros`) REFERENCES `livros` (`idlivros`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `endereco` (
  `idendereco` int NOT NULL AUTO_INCREMENT,
  `bairro` varchar(45) NOT NULL,
  `rua` varchar(45) NOT NULL,
  `numero` varchar(45) NOT NULL,
  `complemento` varchar(45) NOT NULL,
  `cliente_idcliente` int NOT NULL,
  PRIMARY KEY (`idendereco`),
  KEY `fk_endereco_cliente1_idx` (`cliente_idcliente`),
  CONSTRAINT `fk_endereco_cliente1` FOREIGN KEY (`cliente_idcliente`) REFERENCES `cliente` (`idcliente`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `livros` (
  `idlivros` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `autor` varchar(45) NOT NULL,
  `ano` varchar(45) NOT NULL,
  PRIMARY KEY (`idlivros`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;

INSERT INTO `cliente` (`idcliente`, `nome`, `telefone`, `email`) VALUES
(1, 'cliente1', '111-111-111', 'cliente1@gmail.com');
INSERT INTO `cliente` (`idcliente`, `nome`, `telefone`, `email`) VALUES
(2, 'cliente2', '222-222-222', 'cliente2@gmail.com');
INSERT INTO `cliente` (`idcliente`, `nome`, `telefone`, `email`) VALUES
(3, 'cliente3', '333-333-333', 'cliente3@gmail.com');
INSERT INTO `cliente` (`idcliente`, `nome`, `telefone`, `email`) VALUES
(4, 'cliente4', '444-444-444', 'cliente4@gmail.com'),
(5, 'cliente1', '555-555-555', 'cliente5@gmail.com');

INSERT INTO `emprestimo` (`idemprestimo`, `data_de_devolução`, `multa`, `cliente_idcliente`, `livros_idlivros`) VALUES
(1, '30/10/2023', '0', 1, 1);
INSERT INTO `emprestimo` (`idemprestimo`, `data_de_devolução`, `multa`, `cliente_idcliente`, `livros_idlivros`) VALUES
(2, '25/10/2023', '0', 2, 2);
INSERT INTO `emprestimo` (`idemprestimo`, `data_de_devolução`, `multa`, `cliente_idcliente`, `livros_idlivros`) VALUES
(3, '15/10/2023', '4', 3, 3);
INSERT INTO `emprestimo` (`idemprestimo`, `data_de_devolução`, `multa`, `cliente_idcliente`, `livros_idlivros`) VALUES
(4, '10/10/2023', '9', 4, 4),
(5, '30/10/2023', '0', 5, 5);

INSERT INTO `endereco` (`idendereco`, `bairro`, `rua`, `numero`, `complemento`, `cliente_idcliente`) VALUES
(1, 'univesitario', '40', '38', 'casa', 1);
INSERT INTO `endereco` (`idendereco`, `bairro`, `rua`, `numero`, `complemento`, `cliente_idcliente`) VALUES
(2, 'univesitario', '35', '100', 'casa', 2);
INSERT INTO `endereco` (`idendereco`, `bairro`, `rua`, `numero`, `complemento`, `cliente_idcliente`) VALUES
(3, 'univesitario', '41', '50', 'casa', 3);
INSERT INTO `endereco` (`idendereco`, `bairro`, `rua`, `numero`, `complemento`, `cliente_idcliente`) VALUES
(4, 'univesitario', '31', '150', 'casa', 4),
(5, 'univesitario', 'avenida c', '300', 'casa', 5);

INSERT INTO `livros` (`idlivros`, `nome`, `autor`, `ano`) VALUES
(1, 'E Tudo o Vento Levou', 'Margaret Mitchell', '1936');
INSERT INTO `livros` (`idlivros`, `nome`, `autor`, `ano`) VALUES
(2, 'Os sete maridos de Evelyn', ' Hugo Taylor Jenkins Reid', '2017');
INSERT INTO `livros` (`idlivros`, `nome`, `autor`, `ano`) VALUES
(3, 'É assim que acaba', ' Colleen Hoover', '2017');
INSERT INTO `livros` (`idlivros`, `nome`, `autor`, `ano`) VALUES
(4, 'Cinquenta Tons de Cinza', ' E.L. James', '2011'),
(5, 'A Paciente Silenciosa', ' Alex Michaelides', '2019');


/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;