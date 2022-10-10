// let turno = 1;

// function agregarTitulo() {
//   const header = document.getElementById('header')
//   const h2 = document.createElement('h2');
//   h2.innerText = "Turno del jugador: " + nombreJugador(turno);
//   header.appendChild(h2);
// }


// function modificarTitulo() {
//   const h2 = document.querySelector('h2');
//   h2.innerText = "Turno del jugador: " + nombreJugador(turno);
// }

// function crearInicializarMatriz(n) {
//   let mat = [];
//   for (let i = 0; i < n; i++) {
//     let array = [];
//     for (let j = 0; j < n; j++) {
//       array.push(0)
//     }
//     mat.push(array);
//   }
//   const coor1 = (n / 2) - 1;
//   const coor2 = (n / 2);

//   const coordenadaNegro = {
//     p1: {
//       x: coor1,
//       y: coor1
//     },
//     p2: {
//       x: coor2,
//       y: coor2,
//     }
//   };

//   const coordenadaBlanco = {
//     p3: {
//       x: coor1,
//       y: coor2
//     },
//     p4: {
//       x: coor2,
//       y: coor1,
//     }
//   };

//   const { p1, p2 } = coordenadaNegro;
//   const { p3, p4 } = coordenadaBlanco;

//   mat[p1.x][p1.y] = 1;
//   mat[p2.x][p2.y] = 1;
//   mat[p3.x][p3.y] = 2;
//   mat[p4.x][p4.y] = 2;

//   return mat;
// }

// function dibujarTablero(mat, n) {
//   for (let i = 0; i < n; i++) {
//     const tr = document.createElement('tr');
//     tableBody.appendChild(tr);
//     for (let j = 0; j < n; j++) {
//       const td = crearCelda();
//       if (mat[i][j] != 0) {
//         const ficha = crearFicha(mat[i][j]);
//         td.appendChild(ficha);
//       }
//       tr.appendChild(td);
//     }
//   }
// }

// function pintarFicha(player) {
//   switch (player) {
//     case 1:
//       return "black";
//     case 2:
//       return "white"
//     default:
//       return "green";
//   }
// }


// function nombreJugador(player) {
//   switch (player) {
//     case 1:
//       return "Negro";
//     case 2:
//       return "Blanco"
//     default:
//       return "Green";
//   }
// }

// function crearFicha(jugador) {
//   const ficha = document.createElement("div");
//   ficha.classList.add("ficha");
//   ficha.style.backgroundColor = pintarFicha(jugador);
//   ficha.innerText = jugador;
//   ficha.style.color = "transparent";
//   return ficha;
// }


// function crearCelda() {
//   const td = document.createElement('td')
//   td.classList.add('celda')
//   return td;
// }

// function esCeldaValido(mat, i, j) {
//   if (i > 0 && j > 0) {
//     if (mat[i - 1][j - 1] != 0) {
//       return true;
//     }
//   }

//   if (i > 0) {
//     if (mat[i - 1][j] != 0) {
//       return true;
//     }

//   }

//   if (j < mat.length - 1) {
//     if (mat[i][j + 1] != 0) {
//       return true;
//     }

//   }

//   if (i > 0 && j < mat.length - 1) {
//     if (mat[i - 1][j + 1] != 0) {
//       return true;
//     }
//   }


//   if (j > 0) {
//     if (mat[i][j - 1] != 0) {
//       return true;
//     }
//   }


//   if (i < mat.length - 1 && j > 0) {
//     if (mat[i + 1][j - 1] != 0) {
//       return true;
//     }
//   }

//   if (i < mat.length - 1) {
//     if (mat[i + 1][j] != 0) {
//       return true;
//     }
//   }

//   if (i < mat.length - 1 && j < mat.length - 1) {
//     if (mat[i + 1][j + 1] != 0) {
//       return true;
//     }
//   }

//   // Verificar que en la fila que entre dos fichas del mismo color haya una ficha del otro color







//   return false;
// }

// function diagonalValido(mat, esValido) {
//   for (let k = 0; k < mat.length; k++) {
//     if (mat[k][k] != 0) {
//       esValido = false;
//     }
//   }
//   return esValido;
// }

// function columnaValido(mat, j) {

//   let esValido = true;
//   for (let k = 0; k < mat.length; k++) {
//     if (mat[k][j] != 0) {
//       esValido = false;
//     }
//   }
//   return esValido;
// }

// function seleccionarCelda(mat) {
//   const celdas = document.querySelectorAll('.celda');
//   celdas.forEach(celda => {
//     celda.addEventListener('click', async (e) => {
//       let current = e.target;
//       if (!tieneFicha(current)) {
//         const i = current.parentNode.rowIndex;
//         const j = current.cellIndex;

//         if (esCeldaValido(mat, i, j)) {
//           const ficha = crearFicha(turno);
//           current.appendChild(ficha);

//           // pintarOponente(j, mat, i, current);

//           mat[i][j] = turno;
//           turno = turno == 1 ? 2 : 1;
//           modificarTitulo();
//         }
//       }

//       if (gameOver(mat)) {
//         const ganador = decidirGanador(mat);
//         await Swal.fire({
//           position: 'top-end',
//           icon: 'success',
//           title: 'Gana el jugador ' + nombreJugador(ganador),
//           showConfirmButton: false,
//           timer: 1500
//         })

//         location.reload();

//       }
//     })
//   })
// }

// function pintarOponente(j, mat, i, current) {
//   if (j < mat.length - 1) {
//     if (mat[i][j + 1] != 0 && mat[i][j + 1] != turno) {
//       const ficha = current.nextElementSibling.firstElementChild;
//       ficha.style.backgroundColor = pintarFicha(turno);
//       mat[i][j + 1] = turno;
//     }
//   }

//   if (i > 0 && j < mat.length - 1) {
//     if (mat[i - 1][j + 1] != 0 && mat[i - 1][j + 1] != turno) {
//       const ficha = current.parentNode.previousElementSibling.children[j + 1].firstElementChild;
//       ficha.style.backgroundColor = pintarFicha(turno);
//       mat[i - 1][j + 1] = turno;
//     }
//   }

//   if (i > 0) {
//     if (mat[i - 1][j] != 0 && mat[i - 1][j] != turno) {
//       const ficha = current.parentNode.previousElementSibling.children[j].firstElementChild;
//       ficha.style.backgroundColor = pintarFicha(turno);
//       mat[i - 1][j] = turno;
//     }
//   }

//   if (i > 0 && j > 0) {
//     if (mat[i - 1][j - 1] != 0 && mat[i - 1][j - 1] != turno) {
//       const ficha = current.parentNode.previousElementSibling.children[j - 1].firstElementChild;
//       ficha.style.backgroundColor = pintarFicha(turno);
//       mat[i - 1][j - 1] = turno;
//     }
//   }

//   if (j > 0) {
//     if (mat[i][j - 1] != 0 && mat[i][j - 1] != turno) {
//       const ficha = current.previousElementSibling.firstElementChild;
//       ficha.style.backgroundColor = pintarFicha(turno);
//       mat[i][j - 1] = turno;
//     }
//   }

//   if (i < mat.length - 1 && j > 0) {
//     if (mat[i + 1][j - 1] != 0 && mat[i + 1][j - 1] != turno) {
//       const ficha = current.parentNode.nextElementSibling.children[j - 1].firstElementChild;
//       ficha.style.backgroundColor = pintarFicha(turno);
//       mat[i + 1][j - 1] = turno;
//     }
//   }

//   if (i < mat.length - 1) {
//     if (mat[i + 1][j] != 0 && mat[i + 1][j] != turno) {
//       const ficha = current.parentNode.nextElementSibling.children[j].firstElementChild;
//       ficha.style.backgroundColor = pintarFicha(turno);
//       mat[i + 1][j] = turno;
//     }
//   }

//   if (i < mat.length - 1 && j < mat.length - 1) {
//     if (mat[i + 1][j + 1] != 0 && mat[i + 1][j + 1] != turno) {
//       const ficha = current.parentNode.nextElementSibling.children[j + 1].firstElementChild;
//       ficha.style.backgroundColor = pintarFicha(turno);
//       mat[i + 1][j + 1] = turno;
//     }
//   }
// }

// function decidirGanador(mat) {
//   let contadorNegro = 0;
//   let contadorBlanco = 0;
//   for (let i = 0; i < mat.length; i++) {
//     for (let j = 0; j < mat.length; j++) {
//       if (mat[i][j] == 1) {
//         contadorNegro++;
//       } else if (mat[i][j] == 2) {
//         contadorBlanco++;
//       }
//     }
//   }
//   return contadorNegro > contadorBlanco ? 1 : 2;
// }

// function gameOver(mat) {
//   console.log("Tablero Actual:");
//   console.log(mat);
//   for (let i = 0; i < mat.length; i++) {
//     for (let j = 0; j < mat.length; j++) {
//       if (mat[i][j] == 0) {
//         return false;
//       }
//     }
//   }
//   return true;
// }

// function tieneFicha(current) {
//   return current.children.length > 0;
// }

// const table = document.getElementById("othello_table");
// const tableBody = document.getElementById("othello_table_body");

// let n = 8;

// agregarTitulo();

// let mat = crearInicializarMatriz(n);


// dibujarTablero(mat, n)

// seleccionarCelda(mat);




