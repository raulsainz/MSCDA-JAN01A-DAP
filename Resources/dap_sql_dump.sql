--
-- PostgreSQL database dump
--

-- Dumped from database version 11.11 (Debian 11.11-0+deb10u1)
-- Dumped by pg_dump version 11.11 (Debian 11.11-0+deb10u1)

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

--
-- Name: increase_mex_count(); Type: FUNCTION; Schema: public; Owner: remotedap2
--

CREATE FUNCTION public.increase_mex_count() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
	UPDATE icd_10_chapters SET counter_mx = counter_mx + 1 WHERE block = NEW.icd10_chapter;
	RETURN NEW;
END
$$;


ALTER FUNCTION public.increase_mex_count() OWNER TO remotedap2;

--
-- Name: increase_us_count(); Type: FUNCTION; Schema: public; Owner: remotedap2
--

CREATE FUNCTION public.increase_us_count() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
	UPDATE icd_10_chapters SET counter_us = counter_us + 1 WHERE block = NEW.icd10_chapter;
	RETURN NEW;
END
$$;


ALTER FUNCTION public.increase_us_count() OWNER TO remotedap2;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: count_mex; Type: TABLE; Schema: public; Owner: remotedap2
--

CREATE TABLE public.count_mex (
    icd10_chapter character varying(7),
    count bigint
);


ALTER TABLE public.count_mex OWNER TO remotedap2;

--
-- Name: count_us; Type: TABLE; Schema: public; Owner: remotedap2
--

CREATE TABLE public.count_us (
    icd10_chapter character varying(25),
    count bigint
);


ALTER TABLE public.count_us OWNER TO remotedap2;

--
-- Name: count_world; Type: TABLE; Schema: public; Owner: remotedap2
--

CREATE TABLE public.count_world (
    icd10_chapter character varying(7),
    count bigint
);


ALTER TABLE public.count_world OWNER TO remotedap2;

--
-- Name: health_expenditure_per_capita; Type: TABLE; Schema: public; Owner: remotedap2
--

CREATE TABLE public.health_expenditure_per_capita (
    index bigint,
    "Country" text,
    "2017" text,
    "2018" text,
    "2019" text
);


ALTER TABLE public.health_expenditure_per_capita OWNER TO remotedap2;

--
-- Name: icd_10_chapters; Type: TABLE; Schema: public; Owner: remotedap2
--

CREATE TABLE public.icd_10_chapters (
    index bigint,
    chapter integer,
    block text,
    title text,
    counter_mx real DEFAULT 0 NOT NULL,
    counter_us real DEFAULT 0 NOT NULL
);


ALTER TABLE public.icd_10_chapters OWNER TO remotedap2;

--
-- Name: mex_mort; Type: TABLE; Schema: public; Owner: remotedap2
--

CREATE TABLE public.mex_mort (
    _id integer NOT NULL,
    month character(4),
    age_group character varying(255),
    age_group2 character varying(255),
    education character varying(255),
    employement character varying(255),
    marital character varying(255),
    state_death character(4),
    type_death character varying(255),
    place_death character varying(255),
    sex text,
    icd10_block numeric,
    icd10_desc character varying(255),
    icd10_code character varying(3),
    icd10_group character varying(7),
    icd10_chapter character varying(7),
    is_male boolean,
    is_work_related boolean,
    is_foreign boolean,
    is_pregnant boolean,
    is_accident boolean,
    is_cancer boolean,
    is_cvd boolean,
    is_diabetes boolean,
    is_digestive boolean,
    is_mental boolean,
    is_pregnancy boolean,
    is_respiratory boolean,
    is_virus boolean,
    is_suicide boolean,
    is_bacteria boolean
);


ALTER TABLE public.mex_mort OWNER TO remotedap2;

--
-- Name: mex_mort__id_seq; Type: SEQUENCE; Schema: public; Owner: remotedap2
--

CREATE SEQUENCE public.mex_mort__id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mex_mort__id_seq OWNER TO remotedap2;

--
-- Name: mex_mort__id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: remotedap2
--

ALTER SEQUENCE public.mex_mort__id_seq OWNED BY public.mex_mort._id;


--
-- Name: us_mort; Type: TABLE; Schema: public; Owner: remotedap2
--

CREATE TABLE public.us_mort (
    index bigint,
    icd10_code text,
    marital text,
    month text,
    place_death text,
    day_of_death text,
    resident_status text,
    race text,
    age_group text,
    sex text,
    type_death text,
    icd10_chapter character varying(25),
    icd10_block numeric
);


ALTER TABLE public.us_mort OWNER TO remotedap2;

--
-- Name: world_mort; Type: TABLE; Schema: public; Owner: remotedap2
--

CREATE TABLE public.world_mort (
    index bigint,
    country_code text,
    year bigint,
    icd10_code text,
    autopsy text,
    split bigint,
    split_sex bigint,
    forecast bigint,
    month text,
    marital text,
    type_death text,
    sex text,
    day_of_death text,
    race text,
    age_group text,
    icd10_chapter character varying(7),
    icd10_block numeric
);


ALTER TABLE public.world_mort OWNER TO remotedap2;

--
-- Name: mex_mort _id; Type: DEFAULT; Schema: public; Owner: remotedap2
--

ALTER TABLE ONLY public.mex_mort ALTER COLUMN _id SET DEFAULT nextval('public.mex_mort__id_seq'::regclass);


--
-- Data for Name: count_mex; Type: TABLE DATA; Schema: public; Owner: remotedap2
--

COPY public.count_mex (icd10_chapter, count) FROM stdin;
A00–B99	294
C00–D48	1316
D50–D89	43
E00–E90	1689
F00–F99	69
G00–G99	179
H00–H59	2
H60–H95	2
I00–I99	2798
J00–J99	980
K00–K93	929
L00–L99	70
M00–M99	90
N00–N99	376
O00–O99	13
P00–P96	183
Q00–Q99	113
R00–R99	172
V01–Y98	1151
\.


--
-- Data for Name: count_us; Type: TABLE DATA; Schema: public; Owner: remotedap2
--

COPY public.count_us (icd10_chapter, count) FROM stdin;
A00–B99	88
C00–D48	29
D50–D89	1338
E00–E90	73
F00–F99	311
G00–G99	255
H00–H59	537
I00–I99	1897
J00–J99	568
K00–K93	273
L00–L99	8
M00–M99	42
N00–N99	163
O00–O99	4
P00–P96	16
Q00–Q99	15
R00–R99	68
V01–Y98	96
\.


--
-- Data for Name: count_world; Type: TABLE DATA; Schema: public; Owner: remotedap2
--

COPY public.count_world (icd10_chapter, count) FROM stdin;
A00–B99	112
C00–D48	33
D50–D89	1265
E00–E90	50
F00–F99	278
G00–G99	210
H00–H59	490
H60–H95	1
I00–I99	1854
J00–J99	583
K00–K93	252
L00–L99	10
M00–M99	33
N00–N99	158
O00–O99	1
P00–P96	11
Q00–Q99	16
R00–R99	68
V01–Y98	89
\.


--
-- Data for Name: health_expenditure_per_capita; Type: TABLE DATA; Schema: public; Owner: remotedap2
--

COPY public.health_expenditure_per_capita (index, "Country", "2017", "2018", "2019") FROM stdin;
0	Australia	4,711 	4,965 	5,187 
1	Austria	5,360 	5,538 	5,851 
2	Belgium	5,014 	5,103 	5,428 
3	Canada	5,155 	5,287 	5,418 
4	Chile	2,030 	2,126 	2,159 
5	Colombia	1,156 	1,201 	1,213 
6	Czech Republic	2,891 	3,171 	3,428 
7	Denmark	5,107 	5,295 	5,568 
8	Estonia	2,217 	2,368 	2,579 
9	Finland	4,222 	4,331 	4,578 
10	France	5,057 	5,154 	5,376 
11	Germany	6,011 	6,224 	6,646 
12	Greece	2,239 	2,266 	2,384 
13	Hungary	2,029 	2,150 	2,222 
14	Iceland	4,167 	4,420 	4,811 
15	Republic of Ireland	4,743 	4,912 	5,276 
16	Israel	2,715 	2,826 	2,932 
17	Italy	3,399 	3,485 	3,649 
18	Japan	4,393 	4,504 	4,823 
19	Korea	2,809 	3,085 	3,384 
20	Latvia	1,680 	1,856 	1,973 
21	Lithuania	2,236 	2,385 	2,638 
22	Luxembourg	5,013 	5,216 	5,558 
23	Mexico	1,119 	1,145 	1,154 
24	Netherlands	5,264 	5,436 	5,765 
25	New Zealand	3,820 	4,025 	4,204 
26	Norway	6,075 	6,283 	6,647 
27	Poland	2,076 	2,114 	2,230 
28	Portugal	2,922 	3,097 	3,379 
29	Slovakia	2,048 	2,142 	2,354 
30	Slovenia	2,853 	3,042 	3,224 
31	Spain	3,322 	3,430 	3,616 
32	Sweden	5,318 	5,434 	5,782 
33	Switzerland	7,037 	7,280 	7,732 
34	Turkey	1,188 	1,224 	1,337 
35	United Kingdom	4,126 	4,290 	4,653 
36	United States	10,213 	10,637 	11,072 
\.


--
-- Data for Name: icd_10_chapters; Type: TABLE DATA; Schema: public; Owner: remotedap2
--

COPY public.icd_10_chapters (index, chapter, block, title, counter_mx, counter_us) FROM stdin;
18	19	S00–T98	Injury, poisoning and certain other consequences of external causes 	0	0
20	21	Z00–Z99	Factors influencing health status and contact with health services 	0	0
21	22	U00–U99	Codes for special purposes 	0	0
1	2	C00–D48	Neoplasms 	1316	0
8	9	I00–I99	Diseases of the circulatory system 	2798	0
17	18	R00–R99	Symptoms, signs and abnormal clinical and laboratory findings, not elsewhere classified 	172	0
7	8	H60–H95	Diseases of the ear and mastoid process 	2	0
16	17	Q00–Q99	Congenital malformations, deformations and chromosomal abnormalities 	113	0
12	13	M00–M99	Diseases of the musculoskeletal system and connective tissue 	90	0
3	4	E00–E90	Endocrine, nutritional and metabolic diseases 	1689	0
15	16	P00–P96	Certain conditions originating in the perinatal period 	183	0
5	6	G00–G99	Diseases of the nervous system 	179	0
4	5	F00–F99	Mental and behavioural disorders 	69	0
11	12	L00–L99	Diseases of the skin and subcutaneous tissue 	70	0
2	3	D50–D89	Diseases of the blood and blood-forming organs and certain disorders involving the immune mechanism 	43	0
9	10	J00–J99	Diseases of the respiratory system 	980	0
6	7	H00–H59	Diseases of the eye and adnexa 	2	0
14	15	O00–O99	Pregnancy, childbirth and the puerperium 	13	0
0	1	A00–B99	Certain infectious and parasitic diseases 	294	0
10	11	K00–K93	Diseases of the digestive system 	929	0
19	20	V01–Y98	External causes of morbidity and mortality 	1151	0
13	14	N00–N99	Diseases of the genitourinary system 	376	0
\.

--
-- Name: mex_mort__id_seq; Type: SEQUENCE SET; Schema: public; Owner: remotedap2
--

SELECT pg_catalog.setval('public.mex_mort__id_seq', 10469, true);


--
-- Name: mex_mort mex_mort_pkey; Type: CONSTRAINT; Schema: public; Owner: remotedap2
--

ALTER TABLE ONLY public.mex_mort
    ADD CONSTRAINT mex_mort_pkey PRIMARY KEY (_id);


--
-- Name: ix_health_expenditure_per_capita_index; Type: INDEX; Schema: public; Owner: remotedap2
--

CREATE INDEX ix_health_expenditure_per_capita_index ON public.health_expenditure_per_capita USING btree (index);


--
-- Name: ix_icd_10_chapters_index; Type: INDEX; Schema: public; Owner: remotedap2
--

CREATE INDEX ix_icd_10_chapters_index ON public.icd_10_chapters USING btree (index);


--
-- Name: ix_us_mort_index; Type: INDEX; Schema: public; Owner: remotedap2
--

CREATE INDEX ix_us_mort_index ON public.us_mort USING btree (index);


--
-- Name: ix_world_mort_index; Type: INDEX; Schema: public; Owner: remotedap2
--

CREATE INDEX ix_world_mort_index ON public.world_mort USING btree (index);


--
-- Name: mex_mort update_mex_count; Type: TRIGGER; Schema: public; Owner: remotedap2
--

CREATE TRIGGER update_mex_count AFTER INSERT ON public.mex_mort FOR EACH ROW EXECUTE PROCEDURE public.increase_mex_count();


--
-- PostgreSQL database dump complete
--

