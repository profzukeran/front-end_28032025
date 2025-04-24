import React, { Component } from 'react';

class UserList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      users: [] // Inicializa a lista vazia
    };
    this.intervalId = null; // Para simular atualização em tempo real
  }

  // Simula a obtenção de dados ao montar o componente
  componentDidMount() {
    console.log('Componente montado!');
    this.setState({ users: ['Alice', 'Bob', 'Charlie'] });

    // Simula novos usuários se conectando a cada 5 segundos
    this.intervalId = setInterval(() => {
      const randomUser = 'User_' + Math.floor(Math.random() * 100);
      this.setState((prevState) => ({
        users: [...prevState.users, randomUser]
      }));
    }, 5000);
  }

  // Detecta atualizações na lista de usuários
  componentDidUpdate(prevProps, prevState) {
    if (prevState.users.length !== this.state.users.length) {
      console.log('Usuários atualizados:', this.state.users);
    }
  }

  // Limpa os dados ao desmontar o componente
  componentWillUnmount() {
    console.log('Desmontando componente, limpando dados...');
    clearInterval(this.intervalId); // Encerra o intervalo
  }

  render() {
    return (
      <div>
        <h1>Usuários Online:</h1>
        <ul>
          {this.state.users.map((user, index) => (
            <li key={index}>{user}</li>
          ))}
        </ul>
      </div>
    );
  }
}

export default UserList;