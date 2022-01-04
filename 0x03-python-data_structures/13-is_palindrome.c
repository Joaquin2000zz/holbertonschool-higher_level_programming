#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * @head: the linked list
 * Return: 1 if it is or 0 if is not
 */

int is_palindrome(listint_t **head)
{
	listint_t *reflection, *current;

	if (!head)
		return (0);
	if (!*head || (*head)->next == NULL)
		return (1);
	reflection = malloc(sizeof(listint_t));
	if (!reflection)
	{
		free(reflection);
		return (-1);
	}
	current = *head;
	while (current->next)
	{
		add_nodeint(&reflection, current->n), current = current->next;
	}
	current = *(head);
	while (current)
	{
		if (reflection->n == current->n)
		{
			free_listint(reflection);
			return (1);
		}
		current = current->next, reflection = reflection->next;
	}
	return (0);
}

/**
 * add_nodeint - adds a new node at the end of a listint_t list.
 * @head: the head of the list
 * @n: the node's content
 * Return: the new header's list
 */

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new_header;

	new_header = malloc(sizeof(listint_t));

	if (!new_header)
	{
		free(new_header);
		return (0);
	}

	new_header->n = n;
	new_header->next = *head;

	*head = new_header;

	return (*head);
}
