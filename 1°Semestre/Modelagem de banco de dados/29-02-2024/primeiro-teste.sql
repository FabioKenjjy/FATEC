create database venda;
use venda;

create table cliente
(cli_cod int primary key,
cli_nome varchar(30));

insert into cliente 
values (1,'Ana');
insert into cliente
values (2,'Roberto');

select * from cliente;