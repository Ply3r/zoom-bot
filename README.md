# zoom-bot

Criei esse bot em python que verifica se está no horário da aula e se estiver ele entra no zoom, 
utilizando reconhecimento de imagem para detectar o ícone do zoom e o botão de entrar.

Ele pode ser utilizado para várias aulas, é só colocar o horário e o código da aula.

## Como Funciona

O bot vai pedir o horário e o código da aula respectivamente, ele vai salvar essa informação em um array e depois de ser inserido uma ou varias informações, ele vai utilizar o horário da primeira informação para checar se o horário informado é maior que o horário atual, se essa afirmação for verdadeira ele vai disparar um script de ir para a pagina inicial, e com o reconhecimento de imagem vai encontrar o ícone do zoom no desktop e abri-lo, e vai escrever o código da aula informado e entrar na aula, depois disso ele vai apagar o primeiro item do array e vai fazer verificações de 5 em 5 minutos para checar o próximo horário, se não tiver mais nenhum horário o bot para.
