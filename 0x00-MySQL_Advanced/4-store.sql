--  script that creates a trigger that decreases the quantity of an item after adding a new order.
create trigger buy_item
after insert on orders
for each row
update items set quantity = quantity - NEW.number where name = NEW.item_name;
