--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Pokedex; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Pokedex" (
    "Número Pokedex" integer NOT NULL,
    "Espécie" character varying(255),
    "Altura" character varying(255),
    "Peso" character varying(255),
    "Tipo" character varying(255),
    "Região" character varying(255)
);


ALTER TABLE public."Pokedex" OWNER TO cateqadmin;

--
-- Data for Name: Pokedex; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."Pokedex" VALUES (1, 'bulbasaur', '7', '69', 'grass poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (2, 'ivysaur', '10', '130', 'grass poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (3, 'venusaur', '20', '1000', 'grass poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (4, 'charmander', '6', '85', 'fire ', 'kanto');
INSERT INTO public."Pokedex" VALUES (5, 'charmeleon', '11', '190', 'fire ', 'kanto');
INSERT INTO public."Pokedex" VALUES (6, 'charizard', '17', '905', 'fire flying ', 'kanto');
INSERT INTO public."Pokedex" VALUES (7, 'squirtle', '5', '90', 'water ', 'kanto');
INSERT INTO public."Pokedex" VALUES (8, 'wartortle', '10', '225', 'water ', 'kanto');
INSERT INTO public."Pokedex" VALUES (9, 'blastoise', '16', '855', 'water ', 'kanto');
INSERT INTO public."Pokedex" VALUES (10, 'caterpie', '3', '29', 'bug ', 'kanto');
INSERT INTO public."Pokedex" VALUES (11, 'metapod', '7', '99', 'bug ', 'kanto');
INSERT INTO public."Pokedex" VALUES (12, 'butterfree', '11', '320', 'bug flying ', 'kanto');
INSERT INTO public."Pokedex" VALUES (13, 'weedle', '3', '32', 'bug poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (14, 'kakuna', '6', '100', 'bug poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (15, 'beedrill', '10', '295', 'bug poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (16, 'pidgey', '3', '18', 'normal flying ', 'kanto');
INSERT INTO public."Pokedex" VALUES (17, 'pidgeotto', '11', '300', 'normal flying ', 'kanto');
INSERT INTO public."Pokedex" VALUES (18, 'pidgeot', '15', '395', 'normal flying ', 'kanto');
INSERT INTO public."Pokedex" VALUES (19, 'rattata', '3', '35', 'normal ', 'kanto');
INSERT INTO public."Pokedex" VALUES (20, 'raticate', '7', '185', 'normal ', 'kanto');
INSERT INTO public."Pokedex" VALUES (21, 'spearow', '3', '20', 'normal flying ', 'kanto');
INSERT INTO public."Pokedex" VALUES (22, 'fearow', '12', '380', 'normal flying ', 'kanto');
INSERT INTO public."Pokedex" VALUES (23, 'ekans', '20', '69', 'poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (24, 'arbok', '35', '650', 'poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (25, 'pikachu', '4', '60', 'electric ', 'kanto');
INSERT INTO public."Pokedex" VALUES (26, 'raichu', '8', '300', 'electric ', 'kanto');
INSERT INTO public."Pokedex" VALUES (27, 'sandshrew', '6', '120', 'ground ', 'kanto');
INSERT INTO public."Pokedex" VALUES (28, 'sandslash', '10', '295', 'ground ', 'kanto');
INSERT INTO public."Pokedex" VALUES (29, 'nidoran-f', '4', '70', 'poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (30, 'nidorina', '8', '200', 'poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (31, 'nidoqueen', '13', '600', 'poison ground ', 'kanto');
INSERT INTO public."Pokedex" VALUES (32, 'nidoran-m', '5', '90', 'poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (33, 'nidorino', '9', '195', 'poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (34, 'nidoking', '14', '620', 'poison ground ', 'kanto');
INSERT INTO public."Pokedex" VALUES (35, 'clefairy', '6', '75', 'fairy ', 'kanto');
INSERT INTO public."Pokedex" VALUES (36, 'clefable', '13', '400', 'fairy ', 'kanto');
INSERT INTO public."Pokedex" VALUES (37, 'vulpix', '6', '99', 'fire ', 'kanto');
INSERT INTO public."Pokedex" VALUES (38, 'ninetales', '11', '199', 'fire ', 'kanto');
INSERT INTO public."Pokedex" VALUES (39, 'jigglypuff', '5', '55', 'normal fairy ', 'kanto');
INSERT INTO public."Pokedex" VALUES (40, 'wigglytuff', '10', '120', 'normal fairy ', 'kanto');
INSERT INTO public."Pokedex" VALUES (41, 'zubat', '8', '75', 'poison flying ', 'kanto');
INSERT INTO public."Pokedex" VALUES (42, 'golbat', '16', '550', 'poison flying ', 'kanto');
INSERT INTO public."Pokedex" VALUES (43, 'oddish', '5', '54', 'grass poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (44, 'gloom', '8', '86', 'grass poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (45, 'vileplume', '12', '186', 'grass poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (46, 'paras', '3', '54', 'bug grass ', 'kanto');
INSERT INTO public."Pokedex" VALUES (47, 'parasect', '10', '295', 'bug grass ', 'kanto');
INSERT INTO public."Pokedex" VALUES (48, 'venonat', '10', '300', 'bug poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (49, 'venomoth', '15', '125', 'bug poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (50, 'diglett', '2', '8', 'ground ', 'kanto');
INSERT INTO public."Pokedex" VALUES (51, 'dugtrio', '7', '333', 'ground ', 'kanto');
INSERT INTO public."Pokedex" VALUES (52, 'meowth', '4', '42', 'normal ', 'kanto');
INSERT INTO public."Pokedex" VALUES (53, 'persian', '10', '320', 'normal ', 'kanto');
INSERT INTO public."Pokedex" VALUES (54, 'psyduck', '8', '196', 'water ', 'kanto');
INSERT INTO public."Pokedex" VALUES (55, 'golduck', '17', '766', 'water ', 'kanto');
INSERT INTO public."Pokedex" VALUES (56, 'mankey', '5', '280', 'fighting ', 'kanto');
INSERT INTO public."Pokedex" VALUES (57, 'primeape', '10', '320', 'fighting ', 'kanto');
INSERT INTO public."Pokedex" VALUES (58, 'growlithe', '7', '190', 'fire ', 'kanto');
INSERT INTO public."Pokedex" VALUES (59, 'arcanine', '19', '1550', 'fire ', 'kanto');
INSERT INTO public."Pokedex" VALUES (60, 'poliwag', '6', '124', 'water ', 'kanto');
INSERT INTO public."Pokedex" VALUES (61, 'poliwhirl', '10', '200', 'water ', 'kanto');
INSERT INTO public."Pokedex" VALUES (62, 'poliwrath', '13', '540', 'water fighting ', 'kanto');
INSERT INTO public."Pokedex" VALUES (63, 'abra', '9', '195', 'psychic ', 'kanto');
INSERT INTO public."Pokedex" VALUES (64, 'kadabra', '13', '565', 'psychic ', 'kanto');
INSERT INTO public."Pokedex" VALUES (65, 'alakazam', '15', '480', 'psychic ', 'kanto');
INSERT INTO public."Pokedex" VALUES (66, 'machop', '8', '195', 'fighting ', 'kanto');
INSERT INTO public."Pokedex" VALUES (67, 'machoke', '15', '705', 'fighting ', 'kanto');
INSERT INTO public."Pokedex" VALUES (68, 'machamp', '16', '1300', 'fighting ', 'kanto');
INSERT INTO public."Pokedex" VALUES (69, 'bellsprout', '7', '40', 'grass poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (70, 'weepinbell', '10', '64', 'grass poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (71, 'victreebel', '17', '155', 'grass poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (72, 'tentacool', '9', '455', 'water poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (73, 'tentacruel', '16', '550', 'water poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (74, 'geodude', '4', '200', 'rock ground ', 'kanto');
INSERT INTO public."Pokedex" VALUES (75, 'graveler', '10', '1050', 'rock ground ', 'kanto');
INSERT INTO public."Pokedex" VALUES (76, 'golem', '14', '3000', 'rock ground ', 'kanto');
INSERT INTO public."Pokedex" VALUES (77, 'ponyta', '10', '300', 'fire ', 'kanto');
INSERT INTO public."Pokedex" VALUES (78, 'rapidash', '17', '950', 'fire ', 'kanto');
INSERT INTO public."Pokedex" VALUES (79, 'slowpoke', '12', '360', 'water psychic ', 'kanto');
INSERT INTO public."Pokedex" VALUES (80, 'slowbro', '16', '785', 'water psychic ', 'kanto');
INSERT INTO public."Pokedex" VALUES (81, 'magnemite', '3', '60', 'electric steel ', 'kanto');
INSERT INTO public."Pokedex" VALUES (82, 'magneton', '10', '600', 'electric steel ', 'kanto');
INSERT INTO public."Pokedex" VALUES (83, 'farfetchd', '8', '150', 'normal flying ', 'kanto');
INSERT INTO public."Pokedex" VALUES (84, 'doduo', '14', '392', 'normal flying ', 'kanto');
INSERT INTO public."Pokedex" VALUES (85, 'dodrio', '18', '852', 'normal flying ', 'kanto');
INSERT INTO public."Pokedex" VALUES (86, 'seel', '11', '900', 'water ', 'kanto');
INSERT INTO public."Pokedex" VALUES (87, 'dewgong', '17', '1200', 'water ice ', 'kanto');
INSERT INTO public."Pokedex" VALUES (88, 'grimer', '9', '300', 'poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (89, 'muk', '12', '300', 'poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (90, 'shellder', '3', '40', 'water ', 'kanto');
INSERT INTO public."Pokedex" VALUES (91, 'cloyster', '15', '1325', 'water ice ', 'kanto');
INSERT INTO public."Pokedex" VALUES (92, 'gastly', '13', '1', 'ghost poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (93, 'haunter', '16', '1', 'ghost poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (94, 'gengar', '15', '405', 'ghost poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (95, 'onix', '88', '2100', 'rock ground ', 'kanto');
INSERT INTO public."Pokedex" VALUES (96, 'drowzee', '10', '324', 'psychic ', 'kanto');
INSERT INTO public."Pokedex" VALUES (97, 'hypno', '16', '756', 'psychic ', 'kanto');
INSERT INTO public."Pokedex" VALUES (98, 'krabby', '4', '65', 'water ', 'kanto');
INSERT INTO public."Pokedex" VALUES (99, 'kingler', '13', '600', 'water ', 'kanto');
INSERT INTO public."Pokedex" VALUES (100, 'voltorb', '5', '104', 'electric ', 'kanto');
INSERT INTO public."Pokedex" VALUES (101, 'electrode', '12', '666', 'electric ', 'kanto');
INSERT INTO public."Pokedex" VALUES (102, 'exeggcute', '4', '25', 'grass psychic ', 'kanto');
INSERT INTO public."Pokedex" VALUES (103, 'exeggutor', '20', '1200', 'grass psychic ', 'kanto');
INSERT INTO public."Pokedex" VALUES (104, 'cubone', '4', '65', 'ground ', 'kanto');
INSERT INTO public."Pokedex" VALUES (105, 'marowak', '10', '450', 'ground ', 'kanto');
INSERT INTO public."Pokedex" VALUES (106, 'hitmonlee', '15', '498', 'fighting ', 'kanto');
INSERT INTO public."Pokedex" VALUES (107, 'hitmonchan', '14', '502', 'fighting ', 'kanto');
INSERT INTO public."Pokedex" VALUES (108, 'lickitung', '12', '655', 'normal ', 'kanto');
INSERT INTO public."Pokedex" VALUES (109, 'koffing', '6', '10', 'poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (110, 'weezing', '12', '95', 'poison ', 'kanto');
INSERT INTO public."Pokedex" VALUES (111, 'rhyhorn', '10', '1150', 'ground rock ', 'kanto');
INSERT INTO public."Pokedex" VALUES (112, 'rhydon', '19', '1200', 'ground rock ', 'kanto');
INSERT INTO public."Pokedex" VALUES (113, 'chansey', '11', '346', 'normal ', 'kanto');
INSERT INTO public."Pokedex" VALUES (114, 'tangela', '10', '350', 'grass ', 'kanto');
INSERT INTO public."Pokedex" VALUES (115, 'kangaskhan', '22', '800', 'normal ', 'kanto');
INSERT INTO public."Pokedex" VALUES (116, 'horsea', '4', '80', 'water ', 'kanto');
INSERT INTO public."Pokedex" VALUES (117, 'seadra', '12', '250', 'water ', 'kanto');
INSERT INTO public."Pokedex" VALUES (118, 'goldeen', '6', '150', 'water ', 'kanto');
INSERT INTO public."Pokedex" VALUES (119, 'seaking', '13', '390', 'water ', 'kanto');
INSERT INTO public."Pokedex" VALUES (120, 'staryu', '8', '345', 'water ', 'kanto');
INSERT INTO public."Pokedex" VALUES (121, 'starmie', '11', '800', 'water psychic ', 'kanto');
INSERT INTO public."Pokedex" VALUES (122, 'mr-mime', '13', '545', 'psychic fairy ', 'kanto');
INSERT INTO public."Pokedex" VALUES (123, 'scyther', '15', '560', 'bug flying ', 'kanto');
INSERT INTO public."Pokedex" VALUES (124, 'jynx', '14', '406', 'ice psychic ', 'kanto');
INSERT INTO public."Pokedex" VALUES (125, 'electabuzz', '11', '300', 'electric ', 'kanto');
INSERT INTO public."Pokedex" VALUES (126, 'magmar', '13', '445', 'fire ', 'kanto');
INSERT INTO public."Pokedex" VALUES (127, 'pinsir', '15', '550', 'bug ', 'kanto');
INSERT INTO public."Pokedex" VALUES (128, 'tauros', '14', '884', 'normal ', 'kanto');
INSERT INTO public."Pokedex" VALUES (129, 'magikarp', '9', '100', 'water ', 'kanto');
INSERT INTO public."Pokedex" VALUES (130, 'gyarados', '65', '2350', 'water flying ', 'kanto');
INSERT INTO public."Pokedex" VALUES (131, 'lapras', '25', '2200', 'water ice ', 'kanto');
INSERT INTO public."Pokedex" VALUES (132, 'ditto', '3', '40', 'normal ', 'kanto');
INSERT INTO public."Pokedex" VALUES (133, 'eevee', '3', '65', 'normal ', 'kanto');
INSERT INTO public."Pokedex" VALUES (134, 'vaporeon', '10', '290', 'water ', 'kanto');
INSERT INTO public."Pokedex" VALUES (135, 'jolteon', '8', '245', 'electric ', 'kanto');
INSERT INTO public."Pokedex" VALUES (136, 'flareon', '9', '250', 'fire ', 'kanto');
INSERT INTO public."Pokedex" VALUES (137, 'porygon', '8', '365', 'normal ', 'kanto');
INSERT INTO public."Pokedex" VALUES (138, 'omanyte', '4', '75', 'rock water ', 'kanto');
INSERT INTO public."Pokedex" VALUES (139, 'omastar', '10', '350', 'rock water ', 'kanto');
INSERT INTO public."Pokedex" VALUES (140, 'kabuto', '5', '115', 'rock water ', 'kanto');
INSERT INTO public."Pokedex" VALUES (141, 'kabutops', '13', '405', 'rock water ', 'kanto');
INSERT INTO public."Pokedex" VALUES (142, 'aerodactyl', '18', '590', 'rock flying ', 'kanto');
INSERT INTO public."Pokedex" VALUES (143, 'snorlax', '21', '4600', 'normal ', 'kanto');
INSERT INTO public."Pokedex" VALUES (144, 'articuno', '17', '554', 'ice flying ', 'kanto');
INSERT INTO public."Pokedex" VALUES (145, 'zapdos', '16', '526', 'electric flying ', 'kanto');
INSERT INTO public."Pokedex" VALUES (146, 'moltres', '20', '600', 'fire flying ', 'kanto');
INSERT INTO public."Pokedex" VALUES (147, 'dratini', '18', '33', 'dragon ', 'kanto');
INSERT INTO public."Pokedex" VALUES (148, 'dragonair', '40', '165', 'dragon ', 'kanto');
INSERT INTO public."Pokedex" VALUES (149, 'dragonite', '22', '2100', 'dragon flying ', 'kanto');
INSERT INTO public."Pokedex" VALUES (150, 'mewtwo', '20', '1220', 'psychic ', 'kanto');
INSERT INTO public."Pokedex" VALUES (151, 'mew', '4', '40', 'psychic ', 'kanto');


--
-- Name: Pokedex Pokedex_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Pokedex"
    ADD CONSTRAINT "Pokedex_pkey" PRIMARY KEY ("Número Pokedex");


--
-- PostgreSQL database dump complete
--

