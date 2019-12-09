;; SExp - A S-Expression Parser for Python
;; Copyright (C) 2018 Ingo Ruhnke <grumbel@gmail.com>
;;
;; This program is free software: you can redistribute it and/or modify
;; it under the terms of the GNU General Public License as published by
;; the Free Software Foundation, either version 3 of the License, or
;; (at your option) any later version.
;;
;; This program is distributed in the hope that it will be useful,
;; but WITHOUT ANY WARRANTY; without even the implied warranty of
;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;; GNU General Public License for more details.
;;
;; You should have received a copy of the GNU General Public License
;; along with this program.  If not, see <http://www.gnu.org/licenses/>.

(set! %load-path
  (cons* "/ipfs/QmZdLjyRm29uL4Eh4HqkZHvwMMus6zjwQ8EdBtp5JUPT99/guix-cocfree_0.0.0-52-ga8e1798"
         %load-path))

(use-modules (guix packages)
             (guix build-system python)
             ((guix licenses) #:prefix license:)
             (gnu packages python)
             (guix-cocfree utils))

(define %source-dir (dirname (current-filename)))

(define-public python-sexp
  (package
   (name "python-sexp")
   (version (version-from-source %source-dir))
   (source (source-from-source %source-dir))
   (inputs
    `(("python" ,python)))
   (build-system python-build-system)
   (synopsis (synopsis-from-source %source-dir))
   (description (description-from-source %source-dir))
   (home-page (homepage-from-source %source-dir))
   (license license:gpl3+)))

python-sexp

;; EOF ;;
