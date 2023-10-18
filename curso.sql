/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE TABLE `categoria` (
  `idcategoria` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `categoria` varchar(45) NOT NULL,
  PRIMARY KEY (`idcategoria`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `cliente` (
  `idcliente` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `telefone` varchar(45) NOT NULL,
  `tipo` varchar(45) NOT NULL,
  PRIMARY KEY (`idcliente`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `endereco` (
  `idendereco` int NOT NULL AUTO_INCREMENT,
  `cep` varchar(45) NOT NULL,
  `uf` varchar(45) NOT NULL,
  `cidade` varchar(45) NOT NULL,
  `bairro` varchar(45) NOT NULL,
  `rua` varchar(45) NOT NULL,
  `numero` varchar(45) NOT NULL,
  `complemento` varchar(45) NOT NULL,
  `cliente_idcliente` int NOT NULL,
  PRIMARY KEY (`idendereco`),
  KEY `fk_endereco_cliente_idx` (`cliente_idcliente`),
  CONSTRAINT `fk_endereco_cliente` FOREIGN KEY (`cliente_idcliente`) REFERENCES `cliente` (`idcliente`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `produtos` (
  `idprodutos` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `quantidade` varchar(45) NOT NULL,
  `valor` varchar(45) NOT NULL,
  `imposto1` varchar(45) NOT NULL,
  `imposto2` varchar(45) NOT NULL,
  `imposto3` varchar(45) NOT NULL,
  `categoria_idcategoria` int NOT NULL,
  `fabricante_id` int NOT NULL,
  `fornecedor_id` int NOT NULL,
  PRIMARY KEY (`idprodutos`),
  KEY `fk_produtos_categoria1_idx` (`categoria_idcategoria`),
  KEY `fk_produtos_cliente1_idx` (`fabricante_id`),
  KEY `fk_produtos_cliente2_idx` (`fornecedor_id`),
  CONSTRAINT `fk_produtos_categoria1` FOREIGN KEY (`categoria_idcategoria`) REFERENCES `categoria` (`idcategoria`),
  CONSTRAINT `fk_produtos_cliente1` FOREIGN KEY (`fabricante_id`) REFERENCES `cliente` (`idcliente`),
  CONSTRAINT `fk_produtos_cliente2` FOREIGN KEY (`fornecedor_id`) REFERENCES `cliente` (`idcliente`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;

INSERT INTO `categoria` (`idcategoria`, `nome`, `categoria`) VALUES
(3, 'devassa', 'cerveja');
INSERT INTO `categoria` (`idcategoria`, `nome`, `categoria`) VALUES
(4, 'pulseira', 'joias');
INSERT INTO `categoria` (`idcategoria`, `nome`, `categoria`) VALUES
(5, 'whisk', 'destilados');
INSERT INTO `categoria` (`idcategoria`, `nome`, `categoria`) VALUES
(6, 'computadores', 'tecnologia'),
(7, 'chocolates', 'doces'),
(8, 'carros', 'automoveis');

INSERT INTO `cliente` (`idcliente`, `nome`, `email`, `telefone`, `tipo`) VALUES
(1, 'luis', 'luishenrique@gmail.com', '63984686808', 'cli');
INSERT INTO `cliente` (`idcliente`, `nome`, `email`, `telefone`, `tipo`) VALUES
(2, 'pedro', 'pedro@gmail.com', '63984483785', 'for');
INSERT INTO `cliente` (`idcliente`, `nome`, `email`, `telefone`, `tipo`) VALUES
(3, 'ambev', 'ambev@gmail.com', '4563543535', 'fab');
INSERT INTO `cliente` (`idcliente`, `nome`, `email`, `telefone`, `tipo`) VALUES
(4, 'cliente3', 'cliente3@gmail.com', '333-444-222', 'for'),
(5, 'cliente4', 'cliente4@gmail.com', '777-555-222', 'fab'),
(6, 'cliente5', 'cliente5@gmail.com', '888-111-222', 'for'),
(7, 'cliente6', 'cliente6@gmail.com', '999-111-444', 'fab'),
(8, 'cliente7', 'cliente7@gmail.com', '888-222-555', 'for'),
(9, 'cliente8', 'cliente8@gmail.com', '114-666-777', 'fab'),
(10, 'cliente9', 'cliente9@gmail.com', '768-643-897', 'for');

INSERT INTO `endereco` (`idendereco`, `cep`, `uf`, `cidade`, `bairro`, `rua`, `numero`, `complemento`, `cliente_idcliente`) VALUES
(1, '776500', 'TO', 'miracema', 'universitario', '40', '38', 'casa', 1);
INSERT INTO `endereco` (`idendereco`, `cep`, `uf`, `cidade`, `bairro`, `rua`, `numero`, `complemento`, `cliente_idcliente`) VALUES
(2, '77650000', 'TO', 'miracema', 'universitario', '40', '38', 'casa', 2);
INSERT INTO `endereco` (`idendereco`, `cep`, `uf`, `cidade`, `bairro`, `rua`, `numero`, `complemento`, `cliente_idcliente`) VALUES
(3, '7794598', 'TO', 'palmas', 'universitario', '06', '38', 'predio', 3);
INSERT INTO `endereco` (`idendereco`, `cep`, `uf`, `cidade`, `bairro`, `rua`, `numero`, `complemento`, `cliente_idcliente`) VALUES
(4, '7794598', 'TO', 'palmas', 'universitario', '06', '38', 'predio', 4),
(5, '7794598', 'TO', 'palmas', 'universitario', '06', '38', 'predio', 5),
(6, '7794598', 'TO', 'palmas', 'universitario', '06', '38', 'predio', 6),
(7, '7794598', 'TO', 'palmas', 'universitario', '06', '38', 'predio', 7),
(8, '7794598', 'TO', 'palmas', 'universitario', '06', '38', 'predio', 8),
(9, '7794598', 'TO', 'palmas', 'universitario', '06', '38', 'predio', 9),
(10, '7794598', 'TO', 'palmas', 'universitario', '06', '38', 'predio', 10);

INSERT INTO `produtos` (`idprodutos`, `nome`, `quantidade`, `valor`, `imposto1`, `imposto2`, `imposto3`, `categoria_idcategoria`, `fabricante_id`, `fornecedor_id`) VALUES
(1, 'devassa', '500', '3,5', '12', '6', '3', 3, 3, 2);
INSERT INTO `produtos` (`idprodutos`, `nome`, `quantidade`, `valor`, `imposto1`, `imposto2`, `imposto3`, `categoria_idcategoria`, `fabricante_id`, `fornecedor_id`) VALUES
(2, 'opala', '10', '60.000', '12', '6', '3', 8, 7, 4);
INSERT INTO `produtos` (`idprodutos`, `nome`, `quantidade`, `valor`, `imposto1`, `imposto2`, `imposto3`, `categoria_idcategoria`, `fabricante_id`, `fornecedor_id`) VALUES
(3, 'bombom', '500', '10', '12', '6', '3', 7, 5, 6);
INSERT INTO `produtos` (`idprodutos`, `nome`, `quantidade`, `valor`, `imposto1`, `imposto2`, `imposto3`, `categoria_idcategoria`, `fabricante_id`, `fornecedor_id`) VALUES
(4, 'asus', '100', '5000', '12', '6', '3', 6, 9, 10),
(5, 'black label', '500', '200', '12', '6', '3', 5, 7, 6),
(6, 'rolex', '50', '100000', '12', '6', '3', 4, 9, 10);


/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;