prompt PL/SQL Developer import file
prompt Created on miércoles, 1 de abril de 2026 by PC
set feedback off
set define off
prompt Creating CONTACTOS...
create table CONTACTOS
(
  ID_CONTACTO NUMBER(3) not null,
  NOMBRE      VARCHAR2(100),
  EMAIL       VARCHAR2(100),
  MENSAJE     VARCHAR2(500),
  TIPO        VARCHAR2(50)
)
tablespace SYSTEM
  pctfree 10
  pctused 40
  initrans 1
  maxtrans 255
  storage
  (
    initial 64K
    next 1M
    minextents 1
    maxextents unlimited
  );
alter table CONTACTOS
  add primary key (ID_CONTACTO)
  using index 
  tablespace SYSTEM
  pctfree 10
  initrans 2
  maxtrans 255
  storage
  (
    initial 64K
    next 1M
    minextents 1
    maxextents unlimited
  );

prompt Disabling triggers for CONTACTOS...
alter table CONTACTOS disable all triggers;
prompt Loading CONTACTOS...
insert into CONTACTOS (ID_CONTACTO, NOMBRE, EMAIL, MENSAJE, TIPO)
values (2, 'ricardo', 'nanahs@bdbdb', 'quiero trabjar ', 'TRABAJO');
insert into CONTACTOS (ID_CONTACTO, NOMBRE, EMAIL, MENSAJE, TIPO)
values (1, 'Alexander', 'amfpunkrock@gmail.com', 'hola estoy interesado en trabajar aqui', 'CONSULTA');
insert into CONTACTOS (ID_CONTACTO, NOMBRE, EMAIL, MENSAJE, TIPO)
values (4, 'alex', 'alex@hahah', 'hola', 'CONSULTA');
commit;
prompt 3 records loaded
prompt Enabling triggers for CONTACTOS...
alter table CONTACTOS enable all triggers;
set feedback on
set define on
prompt Done.
