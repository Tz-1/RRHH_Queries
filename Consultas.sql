select p.firstname, p.lastname, d.name
from person p 
join employeedepartmenthistory e on p.businessentityid = e.businessentityid 
join department d on e.departmentid = d.departmentid ;

select p.firstname, p.lastname, d.name
from person p 
join employeedepartmenthistory e on p.businessentityid = e.businessentityid 
join department d on e.departmentid = d.departmentid 
where d.name = 'Engineering';

select d.groupname, count(d.groupname) as cantidad_departamentos
from department d
group by d.groupname ;

select s.name, count(e.shiftid) as cantidad_empleados
from shift s
join employeedepartmenthistory e ON s.shiftid = e.shiftid 
group by s.name  order by s.name ;