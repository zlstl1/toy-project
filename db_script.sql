DROP TABLE badge;
CREATE TABLE badge(
	badgeId NUMBER(10) NOT NULL,
	image VARCHAR2(1024),
	badgeName VARCHAR2(64),
	content VARCHAR2(64),
	detailContent VARCHAR2(128),
	createDt date default sysdate,
	CONSTRAINT badge_pk PRIMARY KEY (badgeId)
);

DROP SEQUENCE badge_seq;
CREATE SEQUENCE badge_seq START WITH 1 INCREMENT BY 1 MAXVALUE 9999999999 CYCLE NOCACHE;

DROP TABLE usertb;
CREATE TABLE usertb(
	userId NUMBER(10) NOT NULL,
	userName VARCHAR2(64),
	email VARCHAR2(64),
	team VARCHAR2(64),
	position VARCHAR2(64),
	CONSTRAINT usertb_pk PRIMARY KEY (userId)
);

DROP SEQUENCE user_seq;
CREATE SEQUENCE user_seq START WITH 1 INCREMENT BY 1 MAXVALUE 9999999999 CYCLE NOCACHE;

DROP TABLE userBadge;
CREATE TABLE userBadge(
	badgeId NUMBER(10) NOT NULL,
	userId NUMBER(10) NOT NULL,
	createDt date default sysdate,
	CONSTRAINT userBadge_pk PRIMARY KEY (badgeId, userId)
);

COMMIT;
