prompt PL/SQL Developer import file
prompt Created on miércoles, 1 de abril de 2026 by PC
set feedback off
set define off
prompt Creating CLIENTES...
create table CLIENTES
(
  DNI    VARCHAR2(10) not null,
  NOMBRE VARCHAR2(100),
  EMAIL  VARCHAR2(100),
  CIUDAD VARCHAR2(50)
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
alter table CLIENTES
  add primary key (DNI)
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

prompt Disabling triggers for CLIENTES...
alter table CLIENTES disable all triggers;
prompt Loading CLIENTES...
insert into CLIENTES (DNI, NOMBRE, EMAIL, CIUDAD)
values ('12345678A', 'Juan Garcia', 'juan@gmail.com', 'Madrid');
insert into CLIENTES (DNI, NOMBRE, EMAIL, CIUDAD)
values ('87654321B', 'Maria Lopez', 'maria@gmail.com', 'Barcelona');
insert into CLIENTES (DNI, NOMBRE, EMAIL, CIUDAD)
values ('11223344C', 'Pedro Martinez', 'pedro@gmail.com', 'Sevilla');
insert into CLIENTES (DNI, NOMBRE, EMAIL, CIUDAD)
values ('44332211D', 'Ana Fernandez', 'ana@gmail.com', 'Valencia');
insert into CLIENTES (DNI, NOMBRE, EMAIL, CIUDAD)
values ('55667788E', 'Luis Urrutia', 'luisb@gmail.com', 'Bilbao');
commit;
prompt 5 records loaded
prompt Enabling triggers for CLIENTES...
alter table CLIENTES enable all triggers;
set feedback on
set define on
prompt Done.
