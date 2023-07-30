select * from auth_user;

select name, description, question, answer, author_id, c.date_created from cards_card c
join cards_cardset cs on c.card_set_id = cs.id
where author_id = 1

select * from cards_cardset;