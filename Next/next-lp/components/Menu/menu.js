import './menu.module.css'
import {Sidebar, LogoText} from 'react-sidebar-ui'
import 'react-sidebar-ui/dist/index.css';
import { makeStyles } from '@material-ui/core/styles';
import Avatar from '@material-ui/core/Avatar';

const useStyles = makeStyles((theme) => ({
    root: {   
      display: 'flex',
      '& > *': {
        margin: theme.spacing(1),
      },
    },
    small: {
      width: theme.spacing(3),
      height: theme.spacing(3),
    },
    large: {
      width: theme.spacing(15),
      height: theme.spacing(15),
      margin: '3pc auto auto auto',
    },
  }));

export default function Menu() {
  const classes = useStyles();
  return (
    <div>
        <Sidebar bgColor='black' isCollapsed={false}>
        <Avatar
            alt="Remy Sharp"
            src="/images/avatar.png"
            className={classes.large}
        />
        
        <LogoText>Oscar da Silva</LogoText>
      </Sidebar>
    </div>
  )
};
