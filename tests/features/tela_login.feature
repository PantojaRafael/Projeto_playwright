# Created by rafael.pantoja at 11/11/2023

Feature: Fazer uma validação no google, onde eu vou acessar a página do Google e
  digitar o meu nome e fazer uma validação se existe algum nome igual ao meu.

  Scenario: Acessar a pagina do Google e pesquisa se o meu nome existe
    Given Estou na pagina do google
    When farei uma pesquisa usando o meu nome
    Then farei uma validação para saber se o meu nome existe


  Scenario: Entrar em uma pagina chamada "Saucedemo"
    Given Estou na pagina de login saucedemo
    When Preencho o username e password
    Then faço login