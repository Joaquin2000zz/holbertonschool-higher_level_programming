#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head, *new_node = NULL;

	if (!head)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number, new_node->next = NULL;
	if ((*head)->next == NULL)
	{
		if ((*head)->n < new_node->n)
			(*head)->next = new_node;
		else
			new_node->next = *head, *head = new_node;
		return (new_node);
	}
	while (tmp->next)
	{
		if (tmp->n <= number)
		{
			if (tmp->next)
				tmp = tmp->next;
			else
			{
				new_node->next = tmp->next, tmp->next = new_node;
				return (new_node);
			}
		}
		if (tmp->next->n >= number)
		{
			new_node->next = tmp->next, tmp->next = new_node;
			
			return (new_node);
		}
	}
	return (new_node);
}
