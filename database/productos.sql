prompt PL/SQL Developer import file
prompt Created on miércoles, 1 de abril de 2026 by PC
set feedback off
set define off
prompt Creating PRODUCTOS...
create table PRODUCTOS
(
  ID_PRODUCTO  NUMBER(3) not null,
  NOMBRE       VARCHAR2(100),
  PRECIO       NUMBER(8,2),
  FOTO         VARCHAR2(100),
  ID_CATEGORIA NUMBER(3)
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
alter table PRODUCTOS
  add primary key (ID_PRODUCTO)
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

prompt Disabling triggers for PRODUCTOS...
alter table PRODUCTOS disable all triggers;
prompt Loading PRODUCTOS...
insert into PRODUCTOS (ID_PRODUCTO, NOMBRE, PRECIO, FOTO, ID_CATEGORIA)
values (1, 'INCA KOLA', 2.5, 'inca.jpg', 1);
insert into PRODUCTOS (ID_PRODUCTO, NOMBRE, PRECIO, FOTO, ID_CATEGORIA)
values (2, 'CERVEZA CUZQUEÑA', 3, 'cuzquena.jpg', 1);
insert into PRODUCTOS (ID_PRODUCTO, NOMBRE, PRECIO, FOTO, ID_CATEGORIA)
values (3, 'MAZAMORRA MORADA', 4, 'mazamorra.jpg', 3);
insert into PRODUCTOS (ID_PRODUCTO, NOMBRE, PRECIO, FOTO, ID_CATEGORIA)
values (4, 'AJI AMARILLO', 1.8, 'aji.jpg', 2);
insert into PRODUCTOS (ID_PRODUCTO, NOMBRE, PRECIO, FOTO, ID_CATEGORIA)
values (5, 'TURRONES', 5, 'turrones.jpg', 3);
commit;
prompt 5 records loaded
prompt Enabling triggers for PRODUCTOS...
alter table PRODUCTOS enable all triggers;
set feedback on
set define on
prompt Done.
