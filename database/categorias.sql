prompt PL/SQL Developer import file
prompt Created on miércoles, 1 de abril de 2026 by PC
set feedback off
set define off
prompt Creating CATEGORIAS...
create table CATEGORIAS
(
  ID_CATEGORIA NUMBER(3) not null,
  NOMBRE       VARCHAR2(50)
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
alter table CATEGORIAS
  add primary key (ID_CATEGORIA)
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

prompt Disabling triggers for CATEGORIAS...
alter table CATEGORIAS disable all triggers;
prompt Loading CATEGORIAS...
insert into CATEGORIAS (ID_CATEGORIA, NOMBRE)
values (1, 'Bebidas');
insert into CATEGORIAS (ID_CATEGORIA, NOMBRE)
values (2, 'Salsas y Condimentos');
insert into CATEGORIAS (ID_CATEGORIA, NOMBRE)
values (3, 'Dulces y postres');
commit;
prompt 3 records loaded
prompt Enabling triggers for CATEGORIAS...
alter table CATEGORIAS enable all triggers;
set feedback on
set define on
prompt Done.
