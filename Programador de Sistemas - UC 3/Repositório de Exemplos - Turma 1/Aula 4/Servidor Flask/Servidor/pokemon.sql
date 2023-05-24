--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1
-- Dumped by pg_dump version 15.1

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
-- Name: Pokemons; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Pokemons" (
    "Id" integer NOT NULL,
    "Espécie" character varying(255) NOT NULL,
    "Peso" double precision,
    "Altura" double precision,
    "Tipo" character varying(255) NOT NULL
);


ALTER TABLE public."Pokemons" OWNER TO postgres;

--
-- Data for Name: Pokemons; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Pokemons" ("Id", "Espécie", "Peso", "Altura", "Tipo") FROM stdin;
1	bulbasaur	69	7	/grass/poison
2	ivysaur	130	10	/grass/poison
3	venusaur	1000	20	/grass/poison
4	charmander	85	6	/fire
5	charmeleon	190	11	/fire
6	charizard	905	17	/fire/flying
7	squirtle	90	5	/water
8	wartortle	225	10	/water
9	blastoise	855	16	/water
10	caterpie	29	3	/bug
11	metapod	99	7	/bug
12	butterfree	320	11	/bug/flying
13	weedle	32	3	/bug/poison
14	kakuna	100	6	/bug/poison
15	beedrill	295	10	/bug/poison
16	pidgey	18	3	/normal/flying
17	pidgeotto	300	11	/normal/flying
18	pidgeot	395	15	/normal/flying
19	rattata	35	3	/normal
20	raticate	185	7	/normal
21	spearow	20	3	/normal/flying
22	fearow	380	12	/normal/flying
23	ekans	69	20	/poison
24	arbok	650	35	/poison
25	pikachu	60	4	/electric
26	raichu	300	8	/electric
27	sandshrew	120	6	/ground
28	sandslash	295	10	/ground
29	nidoran-f	70	4	/poison
30	nidorina	200	8	/poison
31	nidoqueen	600	13	/poison/ground
32	nidoran-m	90	5	/poison
33	nidorino	195	9	/poison
34	nidoking	620	14	/poison/ground
35	clefairy	75	6	/fairy
36	clefable	400	13	/fairy
37	vulpix	99	6	/fire
38	ninetales	199	11	/fire
39	jigglypuff	55	5	/normal/fairy
40	wigglytuff	120	10	/normal/fairy
41	zubat	75	8	/poison/flying
42	golbat	550	16	/poison/flying
43	oddish	54	5	/grass/poison
44	gloom	86	8	/grass/poison
45	vileplume	186	12	/grass/poison
46	paras	54	3	/bug/grass
47	parasect	295	10	/bug/grass
48	venonat	300	10	/bug/poison
49	venomoth	125	15	/bug/poison
50	diglett	8	2	/ground
51	dugtrio	333	7	/ground
52	meowth	42	4	/normal
53	persian	320	10	/normal
54	psyduck	196	8	/water
55	golduck	766	17	/water
56	mankey	280	5	/fighting
57	primeape	320	10	/fighting
58	growlithe	190	7	/fire
59	arcanine	1550	19	/fire
60	poliwag	124	6	/water
61	poliwhirl	200	10	/water
62	poliwrath	540	13	/water/fighting
63	abra	195	9	/psychic
64	kadabra	565	13	/psychic
65	alakazam	480	15	/psychic
66	machop	195	8	/fighting
67	machoke	705	15	/fighting
68	machamp	1300	16	/fighting
69	bellsprout	40	7	/grass/poison
70	weepinbell	64	10	/grass/poison
71	victreebel	155	17	/grass/poison
72	tentacool	455	9	/water/poison
73	tentacruel	550	16	/water/poison
74	geodude	200	4	/rock/ground
75	graveler	1050	10	/rock/ground
76	golem	3000	14	/rock/ground
77	ponyta	300	10	/fire
78	rapidash	950	17	/fire
79	slowpoke	360	12	/water/psychic
80	slowbro	785	16	/water/psychic
81	magnemite	60	3	/electric/steel
82	magneton	600	10	/electric/steel
83	farfetchd	150	8	/normal/flying
84	doduo	392	14	/normal/flying
85	dodrio	852	18	/normal/flying
86	seel	900	11	/water
87	dewgong	1200	17	/water/ice
88	grimer	300	9	/poison
89	muk	300	12	/poison
90	shellder	40	3	/water
91	cloyster	1325	15	/water/ice
92	gastly	1	13	/ghost/poison
93	haunter	1	16	/ghost/poison
94	gengar	405	15	/ghost/poison
95	onix	2100	88	/rock/ground
96	drowzee	324	10	/psychic
97	hypno	756	16	/psychic
98	krabby	65	4	/water
99	kingler	600	13	/water
100	voltorb	104	5	/electric
101	electrode	666	12	/electric
102	exeggcute	25	4	/grass/psychic
103	exeggutor	1200	20	/grass/psychic
104	cubone	65	4	/ground
105	marowak	450	10	/ground
106	hitmonlee	498	15	/fighting
107	hitmonchan	502	14	/fighting
108	lickitung	655	12	/normal
109	koffing	10	6	/poison
110	weezing	95	12	/poison
111	rhyhorn	1150	10	/ground/rock
112	rhydon	1200	19	/ground/rock
113	chansey	346	11	/normal
114	tangela	350	10	/grass
115	kangaskhan	800	22	/normal
116	horsea	80	4	/water
117	seadra	250	12	/water
118	goldeen	150	6	/water
119	seaking	390	13	/water
120	staryu	345	8	/water
121	starmie	800	11	/water/psychic
122	mr-mime	545	13	/psychic/fairy
123	scyther	560	15	/bug/flying
124	jynx	406	14	/ice/psychic
125	electabuzz	300	11	/electric
126	magmar	445	13	/fire
127	pinsir	550	15	/bug
128	tauros	884	14	/normal
129	magikarp	100	9	/water
130	gyarados	2350	65	/water/flying
131	lapras	2200	25	/water/ice
132	ditto	40	3	/normal
133	eevee	65	3	/normal
134	vaporeon	290	10	/water
135	jolteon	245	8	/electric
136	flareon	250	9	/fire
137	porygon	365	8	/normal
138	omanyte	75	4	/rock/water
139	omastar	350	10	/rock/water
140	kabuto	115	5	/rock/water
141	kabutops	405	13	/rock/water
142	aerodactyl	590	18	/rock/flying
143	snorlax	4600	21	/normal
144	articuno	554	17	/ice/flying
145	zapdos	526	16	/electric/flying
146	moltres	600	20	/fire/flying
147	dratini	33	18	/dragon
148	dragonair	165	40	/dragon
149	dragonite	2100	22	/dragon/flying
150	mewtwo	1220	20	/psychic
151	mew	40	4	/psychic
\.


--
-- Name: Pokemons Pokemons_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Pokemons"
    ADD CONSTRAINT "Pokemons_pkey" PRIMARY KEY ("Id");


--
-- PostgreSQL database dump complete
--

