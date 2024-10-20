import { createTheme, responsiveFontSizes } from '@mui/material/styles'
import ThemeVariables from './variables'

declare module '@mui/material/styles' {
  interface Palette {
    darkBlue: Palette['primary'];
  }

  // allow configuration using `createTheme`
  interface PaletteOptions {
    darkBlue?: PaletteOptions['primary'];
  }
}

// Update the Button's color prop options
declare module '@mui/material/Button' {
  interface ButtonPropsColorOverrides {
    darkBlue: true;
  }
}

const { colours, fontSizes, fontWeights } = ThemeVariables

let theme = createTheme({
  palette: {
    primary: {
      main: colours.primary,
      light: colours.primaryLight,
    },
    secondary: {
      main: colours.secondary,
    },
    darkBlue: {
      main: colours.darkBlue,
    },
    background: {
      default: colours.grey,
    },
  },
  typography: {
    h1: {
      fontSize: fontSizes.xxl,
    },
    h2: {
      fontSize: fontSizes.xl,
    },
    h3: {
      fontSize: fontSizes.lg,
    },
    h4: {
      fontSize: fontSizes.lg,
      fontWeight: fontWeights.medium
    },
    h5: {
      fontSize: fontSizes.md,
      fontWeight: fontWeights.bold
    },
    body1: {
      fontSize: fontSizes.sm,
    },
    body2: {
      fontSize: fontSizes.xs,
    },
  },
  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          textTransform: 'none',
        },
        outlined: {
          borderWidth: '2px',
          '&:hover': {
            borderWidth: '2px',
          }
        },
        contained: {
          color: 'white',
        },
      },
      defaultProps: {
        variant: 'contained',
      },
    },
    MuiListItem: {
      styleOverrides: {
        root: {
          paddingLeft: 0,
        }
      }
    },
    MuiLink: {
      styleOverrides: {
        root: {
          textDecoration: 'none',
        }
      }
    },
    MuiTextField: {
      styleOverrides: {
        root: {
          backgroundColor: 'white',
          borderColor: 'white',
        }
      }
    },
    MuiTab: {
      styleOverrides: {
        root: {
          '&:hover': {
            transition: '0.3s ease',
            backgroundColor: colours.white,
            color: colours.primary,
          },
          '&.Mui-selected': {
            backgroundColor: colours.white,
            borderTopLeftRadius: '4px',
            borderTopRightRadius: '4px'
          }
        }
      }
    }
  },
})

theme = responsiveFontSizes(theme)

export default theme
