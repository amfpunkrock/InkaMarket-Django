prompt PL/SQL Developer import file
prompt Created on miércoles, 1 de abril de 2026 by PC
set feedback off
set define off
prompt Creating EMPLEADOS...
create table EMPLEADOS
(
  ID_EMPLEADO NUMBER(3) not null,
  NOMBRE      VARCHAR2(100),
  PUESTO      VARCHAR2(50),
  SALARIO     NUMBER(8,2)
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
alter table EMPLEADOS
  add primary key (ID_EMPLEADO)
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

prompt Disabling triggers for EMPLEADOS...
alter table EMPLEADOS disable all triggers;
prompt Loading EMPLEADOS...
insert into EMPLEADOS (ID_EMPLEADO, NOMBRE, PUESTO, SALARIO)
values (1, 'Carlos Quispe', 'Gerente', 3500);
insert into EMPLEADOS (ID_EMPLEADO, NOMBRE, PUESTO, SALARIO)
values (2, 'Rosa Mamani', 'Vendedor', 1800);
insert into EMPLEADOS (ID_EMPLEADO, NOMBRE, PUESTO, SALARIO)
values (3, 'Luis Huanca', 'Almacen', 1500);
insert into EMPLEADOS (ID_EMPLEADO, NOMBRE, PUESTO, SALARIO)
values (4, 'Ana Condori', 'Cajera', 1600);
insert into EMPLEADOS (ID_EMPLEADO, NOMBRE, PUESTO, SALARIO)
values (5, 'Jorge Flores', 'Repartidor', 1400);
insert into EMPLEADOS (ID_EMPLEADO, NOMBRE, PUESTO, SALARIO)
values (6, 'Maria Quispe', 'Vendedor', 1800);
commit;
prompt 6 records loaded
prompt Enabling triggers for EMPLEADOS...
alter table EMPLEADOS enable all triggers;
set feedback on
set define on
prompt Done.
