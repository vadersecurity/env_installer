if [[ "$TERM" != dumb ]] && (( $+commands[grc] )) ; then

  # Supported commands
  cmds=(
    whois \
    wdiff \
    vmstat \
    uptime \
    ulimit \
    tune2fs \
    traceroute \
    tcpdump \
    systemctl \
    sysctl \
    stat \
    ss \
    sql \
    showmount \
    sensors \
    semanageuser \
    semanagefcontext \
    semanageboolean \
    pv \
    ps \
    proftpd \
    ping2 \
    ping \
    php \
    ntpdate \
    nmap \
    netstat \
    mvn \
    mtr \
    mount \
    lspci \
    lsof \
    lsmod \
    lsblk \
    lsattr \
    ls \
    lolcat \
    log \
    ldap \
    last \
    jobs \
    iwconfig \
    irclog \
    iptables \
    iproute \
    ipneighbor \
    ipaddr \
    ip \
    iostat_sar \
    ifconfig \
    id \
    getsebool \
    getfacl \
    gcc \
    free \
    findmnt \
    fdisk \
    esperanto \
    env \
    du \
    dockerversion \
    dockersearch \
    dockerpull \
    dockerps \
    dockernetwork \
    docker-machinels \
    dockerinfo \
    dockerimages \
    dnf \
    dig \
    diff \
    df \
    cvs \
    configure \
    blkid \
    ant \
  );

  # Set alias for available commands.
  for cmd in $cmds ; do
    if (( $+commands[$cmd] )) ; then
      alias $cmd="grc --colour=auto $(whence $cmd)"
    fi
  done

  # Clean up variables
  unset cmds cmd
fi
