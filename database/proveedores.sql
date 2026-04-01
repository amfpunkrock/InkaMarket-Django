prompt PL/SQL Developer import file
prompt Created on miércoles, 1 de abril de 2026 by PC
set feedback off
set define off
prompt Creating PROVEEDORES...
create table PROVEEDORES
(
  ID_PROVEEDOR NUMBER(3) not null,
  NOMBRE       VARCHAR2(100),
  CONTACTO     VARCHAR2(100),
  PAIS         VARCHAR2(50)
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
alter table PROVEEDORES
  add primary key (ID_PROVEEDOR)
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

prompt Disabling triggers for PROVEEDORES...
alter table PROVEEDORES disable all triggers;
prompt Loading PROVEEDORES...
insert into PROVEEDORES (ID_PROVEEDOR, NOMBRE, CONTACTO, PAIS)
values (1, 'Alimentos Peru SAC', 'info@alimentosperu.com', 'Peru');
insert into PROVEEDORES (ID_PROVEEDOR, NOMBRE, CONTACTO, PAIS)
values (2, 'Bebidas Andinas SRL', 'ventas@bebidasandinas.com', 'Peru');
insert into PROVEEDORES (ID_PROVEEDOR, NOMBRE, CONTACTO, PAIS)
values (3, 'Importaciones Lima', 'lima@importaciones.com', 'Peru');
insert into PROVEEDORES (ID_PROVEEDOR, NOMBRE, CONTACTO, PAIS)
values (4, 'Distribuidora Sur', 'sur@distribuidora.com', 'Peru');
insert into PROVEEDORES (ID_PROVEEDOR, NOMBRE, CONTACTO, PAIS)
values (5, 'Productos Andinos', 'andinos@productos.com', 'Peru');
commit;
prompt 5 records loaded
prompt Enabling triggers for PROVEEDORES...
alter table PROVEEDORES enable all triggers;
set feedback on
set define on
prompt Done.
