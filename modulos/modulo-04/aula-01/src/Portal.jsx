import Botao from './Botao'

function Portal() {
  const name = 'Jan'

  return (
    <div>
      
      <p>{name}</p>
      <p>{ 2 + 2 }</p>
      <p>{name === 'Jan' || name === 'Lucas' ? 'Professor' : 'aluno'}</p>
      <Botao></Botao>
    </div>
  )
}

export default Portal